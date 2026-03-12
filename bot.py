
from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
BOT_TOKEN = "8742294619:AAGxFO632m-b45jvWeTubImJYWnX4WohyRQ"


def start(update, context):
    update.message.reply_text(text=f"Assalom aleykum botimizga xush kelibsiz! Menu bosing --> /menu")

def menu(update, context):
    update.message.reply_text(text=f"Quron tarjimasining nechanchi porasini eshitmoqchisiz tanlang", reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))
def audio(update, context):
    text = update.message.text
    if text == "1-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/1-pora.mp3", "rb"))
        print(text)
    elif text == "2-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/2-pora.mp3", "rb"))
        print(text)
    elif text == "3-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/3-pora.mp3", "rb"))
        print(text)
    elif text == "4-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/4-pora.mp3", "rb"))
        print(text)
    elif text == "5-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/5-pora.mp3", "rb"))
        print(text)
    elif text == "6-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/6-pora.mp3", "rb"))
        print(text)
    elif text == "7-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/7-pora.mp3", "rb"))
        print(text)
    elif text == "8-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/8-pora.mp3", "rb"))
        print(text)
    elif text == "9-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/9-pora.mp3", "rb"))
        print(text)
    elif text == "10-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/10-pora.mp3", "rb"))
        print(text)
    elif text == "11-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/11-pora.mp3", "rb"))
        print(text)
    elif text == "12-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/12-pora.mp3", "rb"))
        print(text)
    elif text == "13-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/13-pora.mp3", "rb"))
        print(text)
    elif text == "14-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/14-pora.mp3", "rb"))
        print(text)
    elif text == "15-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/15-pora.mp3", "rb"))
        print(text)
    elif text == "16-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/16-pora.mp3", "rb"))
        print(text)
    elif text == "17-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/17-pora.mp3", "rb"))
        print(text)
    elif text == "18-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/18-pora.mp3", "rb"))
        print(text)
    elif text == "19-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/19-pora.mp3", "rb"))
        print(text)
    elif text == "20-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/20-pora.mp3", "rb"))
        print(text)
    elif text == "21-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/21-pora.mp3", "rb"))
        print(text)
    elif text == "22-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/22-pora.mp3", "rb"))
        print(text)
    elif text == "23-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/23-pora.mp3", "rb"))
        print(text)
    elif text == "24-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/24-pora.mp3", "rb"))
        print(text)
    elif text == "25-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/25-pora.mp3", "rb"))
        print(text)
    elif text == "26-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/26-pora.mp3", "rb"))
        print(text)
    elif text == "27-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/27-pora.mp3", "rb"))
        print(text)
    elif text == "28-pora":
        update.message.reply_audio(audio=open("/Users/akromburxonov07gmail.com/Downloads/28-pora.mp3", "rb"))
        print(text)

    else:
        update.message.reply_text("Ma'lumot topilmadi.")




buttons= [
    [KeyboardButton("1-pora"),
    KeyboardButton("2-pora"),
    KeyboardButton("3-pora",),
    KeyboardButton("4-pora"),
    KeyboardButton("5-pora"),
    KeyboardButton("6-pora")],
    [KeyboardButton("7-pora"),
    KeyboardButton("8-pora"),
    KeyboardButton("9-pora"),
    KeyboardButton("10-pora"),
    KeyboardButton("11-pora"),
    KeyboardButton("12-pora")],
    [KeyboardButton("13-pora"),
    KeyboardButton("14-pora"),
    KeyboardButton("15-pora"),
    KeyboardButton("16-pora"),
    KeyboardButton("17-pora"),
    KeyboardButton("18-pora")],
    [KeyboardButton("19-pora"),
    KeyboardButton("20-pora"),
    KeyboardButton("21-pora"),
    KeyboardButton("22-pora"),
    KeyboardButton("23-pora"),
    KeyboardButton("24-pora")],
    [KeyboardButton("25-pora"),
    KeyboardButton("26-pora"),
    KeyboardButton("27-pora"),
    KeyboardButton("28-pora"),
    KeyboardButton("29-pora"),
    KeyboardButton("30-pora")]
]

updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("MENU", menu))
dispatcher.add_handler(MessageHandler(Filters.text, audio))
updater.start_polling()
updater.idle()
