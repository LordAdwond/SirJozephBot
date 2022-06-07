import telebot

from config import TOKEN

# bot = telebot.TeleBot("862710843:AAGNoYX8TZxJTXor84FtpkhS6mAvl8B819o")
bot = telebot.TeleBot(TOKEN)
# bot = telebot.

mainChannelLink = "https://www.youtube.com/channel/UC497kRoTbHit8rQNt9eb_4g"
funnyChannelLink = "https://www.youtube.com/channel/UC4jzfYs-SNG1jGETAsawcJA"
tgChannel = "https://t.me/LordAdwondsChannel"
commands = f"\\start\n\\LAlinks\n\\creator\n\\commands\n\\WhoAreYou"


@bot.message_handler(commands=["start"])
def start(message : telebot.types.Message):
    bot.reply_to(message, "I'm alive, Sir!")

@bot.message_handler(commands=["links"])
def links(message : telebot.types.Message):
    # bot.reply_to(message, f"Main channel: {mainChannelLink}\nFunny channel: {funnyChannelLink}\nTelegram channel: {tgChannel}")
    main_YT_channel = telebot.types.InlineKeyboardButton(text="Main YouTube Channel", url=mainChannelLink)
    additional_YT_channel = telebot.types.InlineKeyboardButton(text="Funny YouTube Channel", url=funnyChannelLink)
    telegram_channel = telebot.types.InlineKeyboardButton(text="Telegram Channel", url=tgChannel)

    links_keyboard = telebot.types.InlineKeyboardMarkup()
    links_keyboard.row(main_YT_channel)
    links_keyboard.row(additional_YT_channel)
    links_keyboard.row(telegram_channel)

    bot.send_message(message.chat.id, "Select course: ", reply_markup=links_keyboard)

@bot.message_handler(commands=["creator"])
def creator_name(message : telebot.types.Message):
    bot.reply_to(message, "Lord Adwond")

@bot.message_handler(commands=["commands"])
def commands_list(message : telebot.types.Message):
    bot.reply_to(message, f"There is a list of commands\n\n{commands}")

@bot.message_handler(commands=["select_button"])
def commands_list(message : telebot.types.Message):
    markup = telebot.types.ReplyKeyboardMarkup()
    chat_id = message.chat.id
    button_a = telebot.types.KeyboardButton("a")
    button_b = telebot.types.KeyboardButton("b")
    markup.row( button_a, button_b )
    bot.send_message(chat_id, "Select button", reply_markup=markup)

@bot.message_handler(commands=["WhoAreYou"])
def who_are_you(message : telebot.types.Message):
    bot.reply_to(message, "I'm personal bot of Lord Adwond")

bot.polling()