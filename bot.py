import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Импортируем настройки
import settings

# Логи работы бота
logging.basicConfig(filename="bot.log", level=logging.INFO)

# Прокси
PROXY = {
    "proxy_url": settings.PROXY_URL,
    "urllib3_proxy_kwargs": {"username": settings.PROXY_USERNAME, "password": settings.PROXY_PASSWORD}
}

# Функция обрабатывающая команду /start
def greet_user(update, context):
    print("Вызван /start")
    # Выводим ответ робота в Телеграм
    update.message.reply_text("Приветствую, Хозяин")

# Функция реагирующая на введенные данные в виде текста
def talk_to_me (update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    # Создаем бота
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    # Создаем переменную для более удобного вызова диспетчера
    dp = mybot.dispatcher
    # Добавляем обработчик команды /start
    dp.add_handler(CommandHandler("start", greet_user))
    # Добавляем обработчик для введенного типа данных: текст
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # Добавляем запись в лог-файл о том, что бот запустился
    logging.info("Бот стартовал")
    # Говорим боту отправлять запросы Телеграму на наличие для него сообщений
    mybot.start_polling()
    # Зацикливаем обращения в Телеграм на наличие новых сообщений для бота
    mybot.idle()


if __name__ = "__main__":
    main()
