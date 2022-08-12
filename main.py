from flask import Flask, request
import datetime, calendar, telebot, os

today = calendar.day_name[datetime.date.today().weekday()]

app = Flask(__name__)
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler()
def shedule_message(message):
    if message.text == "Расписание" or message.text == "расписание":
        with open("Shedule.txt", "r", encoding="UTF-8") as file:
            for elem in file:
                if elem.split(":")[0] == today:
                    scedule = elem.split(":")[1]
        res = "\n".join([elem for elem in scedule.split("\t")])
        bot.send_message(message.chat.id, f'Расписание на сегодня:\n{res}')
    else:
        bot.send_message(message.chat.id, f'Я умею только выводить расписание на сегодня 😥')


@app.route("/" + TOKEN, method=["POST"])
def get_message():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "Bot on Python", 200


@app.route("/")
def main():
    bot.remove_webhook()
    bot.set_webhook(url="https://shedulebottelegram.herokuapp.com/" + TOKEN)
    return "Bot on Python", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
