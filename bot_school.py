# Импорт атрибутов из библиотеки telegram.ext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Импорт математической библиотеки
import math

updater = Updater(token="561818364:AAGD-s3-jiZJT9KdVAZlJ1QPf1poBRqtqGE")
dispatcher = updater.dispatcher

def startCommand(bot, update):  # обработка нажатия /start
    bot.send_message(chat_id=update.message.chat_id,
                     text="для решения квадратного уравнения a*x^2+b*x+c=0: введите коэффиценты a,b,c "
                          "через запятую ") #текст выводящийся при нажатие старт

def textMessage(bot, update):  # обработка сообщения от пользователя

    text1 = update.message.text
    List1 = text1.split(',')   # разбитие text1 и создание списка
    a = float (List1[0])     # преобразовать во флоат
    b = float (List1[1])
    c = float (List1[2])
    D = b**2 - 4*a * c     # нахождение дискреминанта
    if D > 0 :             # если дескрименант больше нуля
        x1 = (-b - math.sqrt(D)) / 2*a    # решение квадратного уровнения
        x2 = (-b + math.sqrt(D)) / 2*a
        r = 'x1 = ' + str(x1) + ';' + 'x2 = ' + str(x2)
    elif D == 0 :  # если дескрименант равин нулю
        x = -b / (2 * a)  # решение квадратного уровнения
        r ='x = ' + str(x)
    else :
        r = 'решения нет'
    bot.send_message(chat_id=update.message.chat_id, text=r)  # отправка сообщения ботом




start_handler = CommandHandler("start", startCommand)    # создать обработчик реагирующий на команду "start"
text_handler = MessageHandler(Filters.text, textMessage)  # создать обработчик реагирующий на любой текст

dispatcher.add_handler(start_handler)  # зарегестрируем разработчик реэстре обработчиков
dispatcher.add_handler(text_handler)

updater.start_polling(clean=True)

updater.idle()   # очистка updater



