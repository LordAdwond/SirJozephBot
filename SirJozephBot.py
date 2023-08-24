import telebot
from telebot import types

# additional vars
bot = telebot.TeleBot("862710843:AAGNoYX8TZxJTXor84FtpkhS6mAvl8B819o", parse_mode=None)
order_type = []
workers_ids = [["@LordAdwond", 406191549]]

# markup for work ordering
markup_for_work_ordering = types.ReplyKeyboardMarkup()
button_for_lab = types.InlineKeyboardButton("Замовити лабораторну")
button_for_coursework = types.InlineKeyboardButton("Замовити курсову")
button_for_summary = types.InlineKeyboardButton("Замовити реферат")

markup_for_work_ordering.add(button_for_lab, button_for_coursework)
markup_for_work_ordering.add(button_for_summary)

# markup for work sphere selection
markup_for_work_sphere_selection = types.ReplyKeyboardMarkup()
button_for_programming = types.InlineKeyboardButton("Програмування")
button_for_math = types.InlineKeyboardButton("Математика")

markup_for_work_sphere_selection.add(button_for_programming, button_for_math)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ну привіт")


@bot.message_handler(commands=['order'])
def order_work(message):
    bot.send_message(message.from_user.id, "Вибери вид роботи:", reply_markup=markup_for_work_ordering)


@bot.message_handler(content_types=["text"])
def check_order(message):
    if message.text in ["Замовити лабораторну", "Замовити курсову", "Замовити реферат"]:
        order_type.append(message.text)
        bot.send_message(message.from_user.id, "Вибери напрямок:", reply_markup=markup_for_work_sphere_selection)
    elif message.text in ["Програмування", "Математика"]:
        order_type.append(message.text)
        bot.send_message(message.from_user.id, "Надішли файл з роботою для оцінки")
    else:
        bot.send_message(message.from_user.id, "Повторiть, будь ласка, запит!\nДля цього визвіть команду /order")


@bot.message_handler(content_types=["document"])
def send_order(message):
    order = f"{message.from_user.username}"
    order += f" Вид роботи: {order_type[0].split(' ')[1]} Тематика : {order_type[1]}"

    bot.send_message(workers_ids[0][1], order)
    bot.send_document(workers_ids[0][1], message.document.file_id)

    bot.send_message(message.from_user.id, "Очікуйте відповіді!")


bot.infinity_polling()
