import telebot

from telegram_bot.run_context import global_context

bot = telebot.TeleBot(global_context.BOT_TOKEN)


def error_handler(message, error):
    error_data = f'Catched error in decorator: {str(error)}' \
                 f'\nUser: {str(message.from_user.id)}' \
                 f'\nJSON: {str(message)}'
    chat_id = None
    if type(message) is telebot.types.Message:
        chat_id = message.chat.id
    elif type(message) is telebot.types.CallbackQuery:
        chat_id = message.message.chat.id
    if global_context.IS_PRODUCTION:
        bot.send_message(chat_id, 'Необработанное исключение в работе бота. '
                                  'Админы уже получили информацию об ошибке, но мы будем очень признательны, '
                                  'если ты расскажешь, какая команда вызвала ошибку с помощью /feedback',)
        for admin in global_context.SUDO_USERS:
            bot.send_message(admin, error_data)
    else:
        bot.send_message(chat_id, 'Вернуться в меню')


@bot.message_handler(func=lambda message: True, content_types=['audio', 'photo', 'voice', 'video', 'document',
                                                               'text', 'location', 'contact', 'sticker'])
def absolutely_all_handler(message: telebot.types.Message):
    """
    Агрегатор всех сообщений. Подбирает доступную команду пользователю для заданного сообщения и текущего пути.

    :param message: сообщение, триггер функции

    :return: результат выполнения команды
    """
    chat_id = message.chat.id
    message_author = message.from_user.id
    is_admin = message_author in global_context.SUDO_USERS
    first_word = None
    if message.text is not None:
        lower_message = message.text.lower()
        first_word = lower_message.split()[0]
        if first_word[0] == '/':
            first_word = first_word[1:]

    if first_word == 'start':
        return bot.send_message(chat_id, 'Перезапускаю бота')
    else:
        return bot.send_message(chat_id, 'Кажется я не знаю такой команды. Попробуй /help')
