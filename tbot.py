import telebot
import weather

bot = telebot.TeleBot('6273327730:AAFsKa4fQ099v97L2NFILGfyz_VlNGc8iZQ')
bot.send_message(50853567, 'Готов захватывать мир')
# если бот получил сообщение типа text
@bot.message_handler(content_types=['text'])
def message(info):
    # for key in info.__dict__.keys():
    #     print(key, info.__dict__[key])
    # print(info.chat.id)
    if 'привет' in info.text:
        mes = 'hi'
    elif 'пока' in info.text:
        mes = 'by'
    elif 'погода' in info.text:
        mes = weather.weathersearch()
    else:
        mes = 'Я, Робот'
    bot.send_message(info.chat.id, mes)

bot.polling(none_stop=True)

