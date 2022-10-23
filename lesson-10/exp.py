import logging


from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

reply_keyboard = [['/play', '/rules'],
                  ['/exit']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '5445736222:AAG8IVtzIo4u7LUGQGZpmNZeSadKH0HjnjE'

candy = 0


def start(update, context):
    update.message.reply_text(
        "Привет, давай поиграем)) play-начать игру, rules-правила игры, exit-выход",
        reply_markup=markup
    )


def play(update, context):
    update.message.reply_text(
        "Введите количество конфет"
    )
    return 1


def stop(update, context):
    update.message.reply_text("")
    return ConversationHandler.END


def get_candy(update, context):
    global candy
    try:
        candy = int(update.message.text)
        update.message.reply_text(
            f"В игре {candy} конфет. Вы ходите первым, сколько конфет Вы возьмете"
        )
    except ValueError:
        logging.warning('Ошибка: неверный тип данных')
        update.message.reply_text("Введите число больше 28")
        return 1
    return 2


def user_hod(update, context):
    global candy
    print(candy)
    new_candy = int(update.message.text)
    if new_candy > candy:
        update.message.reply_text("Введите число от 1 до 28")
        return 2
    candy -= new_candy
    if candy <= 28:
        update.message.reply_text("Выиграл БОТ", reply_markup=markup)
        return ConversationHandler.END
    else:

        update.message.reply_text(f"В игре осталось {candy} конфет")
        update.message.reply_text("Я БОТ и я беру 28 конфет")
        candy -= 28
        update.message.reply_text(f"В игре осталось {candy} конфет. Ваш ход!")
        if candy <= 28:
            update.message.reply_text("Вы Победили ", reply_markup=markup)
            return ConversationHandler.END
    return 2


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


def rules(update, context):
    update.message.reply_text(
        "Здесь будут правила игры")


def exit(update, context):
    update.message.reply_text("Пока-пока!")


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    play_handler = ConversationHandler(

        entry_points=[CommandHandler('play', play)],

        states={

            1: [MessageHandler(Filters.text & ~Filters.command, get_candy)],

            2: [MessageHandler(Filters.text & ~Filters.command, user_hod)],
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("exit", exit))

    dp.add_handler(play_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
