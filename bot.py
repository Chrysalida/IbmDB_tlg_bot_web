# -*- coding: utf-8 -*-
"""
Public webhook version
"""


from flask import Flask,request
import os
import time
import telebot

#print(os.getcwd())

server=Flask(__name__)

TOKEN = '<YOUR TOKEN HERE>'

bot = telebot.TeleBot(TOKEN)

hi_list=[]
hi_list=['hi','hello','привет','здравствуй','здравствуйте',]

alltranslators='Александров;Васильев;Захаров;'
Tra_list=alltranslators.split(';')

allLanguages={'eng': 'английский','deu': 'немецкий',
             'fra':'французский', 'rus':'русский',
             'ukr':'украинский', 'bel':'белорусский',
             'kat':'грузинский', 'kaz':'казахский',
             'kir':'киргизский', 'tkm':'туркменский',
             'hye':'армянский', 'dan':'датский',
             'taj':'таджикский', 'uzb':'узбекский',
             'pol':'польский', 'ita':'итальянский',
             'esp':'испанский', 'swe':'шведский',}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    mess=""
    mess = message.text.lower()
    if mess in hi_list:
        print('User wrote: ',message.text)
        bot.send_message(message.from_user.id,"Здравствуйте, {}!".format(message.chat.first_name))

    elif message.text=='/help':
        bot.send_message(message.from_user.id,
                        "Напишите язык, например, FRA, чтобы получить список тех, кто им владеет")
        bot.send_message(message.from_user.id,
                        "Напишите языковую пару, например, Rus-deu, чтобы получить список работающих с ней переводчиков")
        bot.send_message(message.from_user.id,
                        "Напишите мне фамилию переводчика, чтобы узнать о нем побольше")
        bot.send_message(message.from_user.id,
                        "Напишите /lang, чтобы получить список языков")
        print('User asked me for help')

    else:
        bot.send_message(message.from_user.id,'Sorry, dear {}! \n I cannot understand you'.format(message.chat.first_name))
        bot.send_message(message.from_user.id,'I would recommend to ask for /help')
        print('User wrote: ',message.text)

@server.route('/'+TOKEN,methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='YOUR URL HERE'+TOKEN)
    return "!", 200

if __name__=="__main__":
    server.run(host="0.0.0.0",port=int(os.environ.get('PORT',5000)))
