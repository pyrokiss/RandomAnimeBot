import telebot
import os
import xml.etree.ElementTree as ET
import random

bot = telebot.TeleBot('1744338340:AAGSJWnPXDNVJbqprHnKNB226LiHDnIysM4')


@bot.message_handler(commands=['filename'])
def get_filename(message):
    path = "XML_file"
    files = os.listdir(path)
    files = [os.path.join(path, file) for file in files]
    files = [file for file in files if os.path.isfile(file)]
    res = max(files, key=os.path.getctime)
    bot.send_message(message.from_user.id, res)

@bot.message_handler(commands=['completed'])
def get_random_anime_completed(message):
    try:
        # temp = os.listdir(path="XML_file")
        tree = ET.parse("XML_file/{}.xml".format(message.from_user.id))
        root = tree.getroot()
        anime_list_comp = []
        for i in range(len(root) - 1):
            if root[i + 1][12].text == "Completed":
                anime_list_comp.append(root[i + 1][1].text)
        r_idx_c = random.randint(0, len(anime_list_comp)-1)
        # print(anime_list[r_idx])
        bot.send_message(message.from_user.id, anime_list_comp[r_idx_c])
    except FileNotFoundError as f:
        bot.send_message(message.from_user.id, "Для начала пришли твой файл!")
    except ValueError as v:
        bot.send_message(message.from_user.id, "Похоже у тебя нет аниме в этой категории.")

@bot.message_handler(commands=['watching'])
def get_random_anime_watching(message):
    try:
        # temp = os.listdir(path="XML_file")
        tree = ET.parse("XML_file/{}.xml".format(message.from_user.id))
        root = tree.getroot()
        anime_list_watching = []
        for i in range(len(root) - 1):
            if root[i + 1][12].text == "Watching":
                anime_list_watching.append(root[i + 1][1].text)
        r_idx_w = random.randint(0, len(anime_list_watching)-1)
        # print(anime_list[r_idx])
        bot.send_message(message.from_user.id, anime_list_watching[r_idx_w])
    except FileNotFoundError as f:
        bot.send_message(message.from_user.id, "Для начала пришли твой файл!")
    except ValueError as v:
        bot.send_message(message.from_user.id, "Похоже у тебя нет аниме в этой категории.")

@bot.message_handler(commands=['plan'])
def get_random_anime_plan(message):
    try:
        # temp = os.listdir(path="XML_file")
        tree = ET.parse("XML_file/{}.xml".format(message.from_user.id))
        root = tree.getroot()
        anime_list_plan = []
        for i in range(len(root) - 1):
            if root[i + 1][12].text == "Plan to Watch":
                anime_list_plan.append(root[i + 1][1].text)
        r_idx_p = random.randint(0, len(anime_list_plan)-1)
        # print(anime_list[r_idx])
        bot.send_message(message.from_user.id, anime_list_plan[r_idx_p])
    except FileNotFoundError as f:
        bot.send_message(message.from_user.id, "Для начала пришли твой файл!")
    except ValueError as v:
        bot.send_message(message.from_user.id, "Похоже у тебя нет аниме в этой категории.")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Я бот для рандомизации вашего аниме листа. Приятно познакомиться, {message.from_user.first_name}')
    bot.send_message(message.from_user.id, 'Для начала работы пришли мне свой аниме лист \nв формате .xml.\nЕго можно взять с сайта MyAnimeList.\nhttps://myanimelist.net/panel.php?go=export')



@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, """Позволь предоставить тебе список команд:
    /completed - выдает случайное просмотренное аниме.
    /watching - выдает случайное аниме, которое ты сейчас смотришь.
    /plan - выдает случайное непросмотренное аниме.""")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        # print(file_info)
        downloaded_file = bot.download_file(file_info.file_path)
        # print(downloaded_file)

        # print(message.document.file_name)
        filename, file_extension = os.path.splitext(str(message.document.file_name))

        if file_extension != ".xml":
            bot.reply_to(message, "Сорри, но это не тот формат")
        else:
            src = 'XML_file/' + "{}.xml".format(message.from_user.id)
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
                # bot.reply_to(message, "{}".format(message.document.file_name))
            bot.reply_to(message, "Пожалуй, я сохраню это")
    except Exception as e:
        bot.reply_to(message, e)





bot.polling(none_stop=True)
