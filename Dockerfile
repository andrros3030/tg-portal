FROM alpine:3.14
FROM python

WORKDIR /app
COPY requirements.txt /app
COPY telegram_bot /app/telegram_bot

RUN python -m pip install -r requirements.txt

EXPOSE 5000
CMD echo "Port exposed, starting server"
CMD python -m telegram_bot.entrypoint