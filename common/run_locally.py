from telegram_bot.run_context import global_context


def run():
    from telegram_bot.main import bot
    bot.remove_webhook()
    bot.infinity_polling()


print(global_context.BOT_TOKEN)
run()
