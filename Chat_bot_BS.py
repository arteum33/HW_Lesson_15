"""
Чат-бот виртуальной приемной компании
Имя чат-бота: @virtual_reception_bot
"""

import random
import telebot
from telebot import types
import re

# Api данные бота в Telegram
TOKEN = '5015904677:AAF6SjgnW5oX4Fr916jAR4XYsIlZFE9rsqM'
BOT_URL = f'https://api.telegram.org/bot{TOKEN}'

bot = telebot.TeleBot(TOKEN)

# welcome speech
welcome_speech = ["Виртуальный помощник рад приветствовать Вас в приемной Business Strategy Team "
                  "агентства IT'S ON"]
briefly_about_us = ['Business Strategy Team оказывает профессиональные комплексные услуги в сфере маркетинга, PR и '
                    'управления онлайн-репутацией.']
# Описание бизнес-процессов компании
text_team_description = ['Что же такое Business Strategy Team? \n'
                         'Мы являемся частью агентства IT’S ON, которое оказывает профессиональные услуги в сфере '
                         'маркетинга, PR  и организации мероприятий по всему миру на протяжении многих лет и имеет '
                         'репутацию надежного партнера среди многочисленных компаний-клиентов. '
                         'Наша команда представлена действующими маркетологами и пиарщиками крупнейших '
                         'международных компаний – лидеров в своем сегменте. Благодаря нашему богатому и успешному '
                         'опыту и владению самыми современными и эффективными методами продвижения брендов, '
                         'товаром и услуг на рынке России мы реализуем проекты различных масштабов и сложности. \n'
                         'Маркетинг 360°, PR и управление онлайн-репутацией – это наша стихия!']

text_benefits = ['Двукратное сокращение издержек на штатный персонал \n'
                'Повышение эффективности инвестиций в маркетинг и PR \n'
                'Сокращение административных издержек \n'
                'Стратегия в короткие сроки \n'
                'Опыт крупнейших международных и российских брендов из различных сфер \n'
                'Современные и эффективные инструменты и практики \n'
                'Высококвалифицированные и практикующие специалисты \n'
                'Повышение инвестиционной привлекательности компании \n'
                'Гибкий и индивидуальный подход \n']

text_activities = ['Внешние коммуникации (PR) \n'
                 'Вывод брендов на рынок \n'
                 'Оптимизация портфеля брендов / продуктов \n'
                 'Продвижение продуктов и услуг \n'
                 'Управление онлайн-репутацией (ORM / SERM) \n']

text_opportunities = ['Оценка потенциала компании и рынков \n'
                      'Подбор потенциальных контрагентов \n'
                      'Разработка стратегий развития бизнеса \n'
                      'Разработка стратегий в области маркетинга \n'
                      'Разработка стратегий в области PR \n'
                      'Разработка стратегий в области управления интернет-репутацией бренда \n'
                      'Подготовка тактических планов и контроль их реализации \n'
                      'Оценка эффективности кампаний и актуализация планов \n'
                      'Формирование команд \n'
                      'Координация команд \n'
                      'Аудиты текущих кампаний, стратегий и подрядчиков \n']

text_expertise = ['Авиация \n' 'Автомобили \n' 'Автомобильные шины \n' 'Масла и Автохимия \n'
                  'E-commerce, Digital \n' 'FMCG \n' 'DIY \n']
text_portfolio = ['Для отправки портфолио работ команды нам нужна дополнительная информация.'] # запросу контактных данных и их проверка
text_contacts = ['Вы можете сохранить себе наши контакты: \n' 'e-mail: strategy@its-on.ru \n' 'телефон: +7-495-142-94-10']

# Приветствие и выбор действий - меню №1
@bot.message_handler(commands = ['start'])
def commаnd_start(message):
    bot.send_message(message.from_user.id, welcome_speech)
    bot.send_message(message.from_user.id, briefly_about_us)

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='ДА', callback_data='да')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='НЕТ', callback_data='нет')
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, text='Хотите продолжить?', reply_markup=keyboard)

# Уточнение намерений пользователя
@bot.callback_query_handler(func=lambda call: True)
def callback_resp(call):
    # Обработка действий меню №1
    if call.data == 'да':
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст
        key_team_description = types.InlineKeyboardButton(text='О нашей команде', callback_data='a')
        # И добавляем кнопку Меню №2 на экран
        keyboard.add(key_team_description)
        key_benefits = types.InlineKeyboardButton(text='Преимущества нашей команды', callback_data='b')
        keyboard.add(key_benefits)
        key_activities = types.InlineKeyboardButton(text='Направления нашей деятельности', callback_data='c')
        keyboard.add(key_activities)
        key_opportunities = types.InlineKeyboardButton(text='Наши возможности', callback_data='d')
        keyboard.add(key_opportunities)
        key_expertise = types.InlineKeyboardButton(text='Сферы профессиональных компетенций', callback_data='e')
        keyboard.add(key_expertise)
        key_portfolio = types.InlineKeyboardButton(text='Получить портфолио', callback_data='f')
        keyboard.add(key_portfolio)
        key_contacts = types.InlineKeyboardButton(text='Контакты', callback_data='g')
        keyboard.add(key_contacts)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(call.message.chat.id, text='Пожалуйста, выберите то, что Вас интересует', reply_markup=keyboard)
    # Ели пользователь решил отказаться от продолжения в Меню №1
    elif call.data == 'нет':
        bot.send_message(call.message.chat.id, 'До новых встреч!')

    # Отработка действий кнопок Меню №2 — вывод выбранных данных
    elif call.data == 'a':
        bot.send_message(call.message.chat.id, text_team_description)
    elif call.data == 'b':
        bot.send_message(call.message.chat.id, text_benefits)
    elif call.data == 'c':
        bot.send_message(call.message.chat.id, text_activities)
    elif call.data == 'd':
        bot.send_message(call.message.chat.id, text_opportunities)
    elif call.data == 'e':
        bot.send_message(call.message.chat.id, text_expertise)
    elif call.data == 'g':
        bot.send_message(call.message.chat.id, text_contacts)
    elif call.data == 'f':
        bot.send_message(call.message.chat.id, text_portfolio)
        if call.data != 0:
            bot.send_message(call.message.chat.id, 'Представьтесь, пожалуйста')

# Сбор контактной информации для отправки портфолио
@bot.message_handler(content_types=['text'])
def get_tel(message):
    # # Условие проверки ввода имени кириллицей
    # if re.findall(r'[а-яёА-яЁ]', message.text):
    #     bot.send_message(message.from_user.id, text='{name}, приятно познакомиться!'.format(name=message.text))
    #     bot.send_message(message.chat.id, 'Ваш номер телефона (например: +7ХХХХХХХХХХ)')
    # # Условие проверки ввода номера телефона
    # elif re.findall(r'\S{1,2}\S?\d{3}\S?\d{7}', message.text):
    #     bot.send_message(message.chat.id, 'Теперь Ваш электронный адрес')
    # # Условие проверки ввода электронной почты
    # elif re.findall(r'([a-zA-Z0-9_.-])@([a-zA-Z0-9_.-]).([a-zA-Z])', message.text):
    #     bot.send_message(message.chat.id, 'Благодарим за уделенное время!')
    #     bot.send_message(message.chat.id, 'В ближайшее время направим Вам портфолио на указанный эл.адрес')
    # else:
    #     bot.send_message(message.chat.id, 'Попробуйте еще раз')

    # Условие проверки ввода электронной почты
    if re.findall(r'([a-zA-Z0-9_.-])@([a-zA-Z0-9_.-]).([a-zA-Z])', message.text):
        bot.send_message(message.chat.id, 'Благодарим за уделенное время!')
        bot.send_message(message.chat.id, 'В ближайшее время направим Вам портфолио на указанный эл.адрес')
    # Условие проверки ввода номера телефона
    elif re.findall(r'\S{1,2}\S?\d{3}\S?\d{7}', message.text):
        bot.send_message(message.chat.id, 'Теперь Ваш электронный адрес')
    # Условие проверки ввода имени кириллицей
    elif re.findall(r'[а-яёА-яЁa-zA-Z]', message.text):
        bot.send_message(message.from_user.id, text='{name}, приятно познакомиться!'.format(name=message.text))
        bot.send_message(message.chat.id, 'Ваш номер телефона (например: +7ХХХХХХХХХХ)')
    else:
        bot.send_message(message.chat.id, 'Попробуйте еще раз')

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)