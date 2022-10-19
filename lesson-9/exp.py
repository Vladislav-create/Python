import sqlite3
import model

from telegram import Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint
from bot_token import token as TOKEN

reply_keyboard = [['/info', '/roll', '/calc', '/stop', '/show', '/add_user'],
                  ['/exit']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

bot_token = TOKEN
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

conn = sqlite3.connect('students2.db', check_same_thread=False)
cursor = conn.cursor()

add_storage = []


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Привет! /info, /roll, /calc, /stop, /show", reply_markup=markup)


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Это бот")


def roll(update, context):
    context.bot.send_message(update.effective_chat.id, text=str(randint(1, 6)))


def calc(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите выражение")
    return 1


def eval_calc(update, context):
    context.bot.send_message(update.effective_chat.id,
                             f'Результат = {eval(update.message.text)}')


def stop(update, context):
    return ConversationHandler.END


calc_handler = ConversationHandler(
    entry_points=[CommandHandler('calc', calc)],

    states={
        1: [MessageHandler(Filters.text & ~ Filters.command, eval_calc)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)


def show_users(update, context):
    data = model.get_contacts(cursor)
    context.bot.send_message(update.effective_chat.id, f'{data}')


def add_user(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f'Введите фамилию'
    )
    print('add_user')
    print(add_storage)
    return 1


def add_name(update, context):
    name = update.message.text
    add_storage.append(name)
    context.bot.send_message(
        update.effective_chat.id,
        f'Введите имя'
    )
    print('add_name')
    print(add_storage)
    return 2


def add_surname(update, context):
    surname = update.message.text
    add_storage.append(surname)
    context.bot.send_message(
        update.effective_chat.id,
        f'Введите телефон'
    )
    print('add_surname')
    print(add_storage)
    return 3


def add_phone(update, context):
    phone = update.message.text
    add_storage.append(phone)
    context.bot.send_message(
        update.effective_chat.id,
        f'Введите комментарий'
    )
    print('add_phone')
    print(add_storage)
    return 4


def add_description(update, context):
    description = update.message.text
    add_storage.append(description)
    model.add_student(add_storage, conn, cursor)
    context.bot.send_message(
        update.effective_chat.id,
        f'Запись добавлена'
    )
    print('add_description')
    print(add_storage)
    add_storage.clear()


add_handler = ConversationHandler(
    entry_points=[CommandHandler('add_user', add_user)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, add_name)],
        2: [MessageHandler(Filters.text & ~Filters.command, add_surname)],
        3: [MessageHandler(Filters.text & ~Filters.command, add_phone)],
        4: [MessageHandler(Filters.text & ~Filters.command, add_description)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)

start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
roll_handler = CommandHandler('roll', roll)
show_handler = CommandHandler('show', show_users)
show_handler = CommandHandler('add_user', add_user)
# add_handler = CommandHandler('add_user', add_user)
# calc_handler = CommandHandler('calc', calc)
# text_handler = MessageHandler(Filters.text & ~ Filters.command, eval_calc)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(roll_handler)
dispatcher.add_handler(calc_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler(add_handler)
# dispatcher.add_handler(text_handler)
updater.start_polling()
updater.idle()
conn.close()
