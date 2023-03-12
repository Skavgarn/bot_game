import telebot
import random

# https://t.me/efefeefefeffbot
bot = telebot.TeleBot("", parse_mode=None)
number = random.randint(1, 1000000)
counter = [0]


@bot.message_handler(content_types=["text"])
def mind(message):
    try:
        mentioned_number = int(message.text)
        counter[0] = counter[0] + 1
        if mentioned_number > number:
            bot.send_message(message.chat.id, f"Нужно меньше чем: {mentioned_number}")
            print(f"{counter}. {mentioned_number} Нужно меньше")
        elif mentioned_number < number:
            bot.send_message(message.chat.id, f"Нужно больше чем: {mentioned_number}")
            print(f"{counter}. {mentioned_number} Нужно больше чем")
        elif mentioned_number == number:
            bot.send_message(message.chat.id,
                             f"Ты победил и приз твой!!! Веное число: {mentioned_number}")
            print(f"{counter}. {mentioned_number} ВЕРНОЕ ЧИСЛО")
    except Exception:
        pass


bot.infinity_polling()
