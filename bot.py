import telebot
import os
import xml.etree.ElementTree as ET
import random
import bs4

bot = telebot.TeleBot('1744338340:AAGSJWnPXDNVJbqprHnKNB226LiHDnIysM4')

def table_anime_html(id):
    file_name = "HTML_file/{}.html".format(id)
    HtmlFile = open(file_name, 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    # print(source_code)
    soup = bs4.BeautifulSoup(source_code, 'html.parser')
    q1 = soup.find_all('td')
    l = []
    for i in range(len(q1)):
        l.append(str(q1[i]).split("\n"))
    # l.append(q1[0])
    # print(l)
    for i in l:
        temp = i
        temp.remove(temp[0])
        temp.remove(temp[-1])
        temp.remove(temp[-1])
        for j in temp:
            if j == '<ul>':
                temp.remove(j)
    for i in l:
        temp = i
        for j in range(len(temp)):
            temp[j] = temp[j].replace("<h3>", '')
            temp[j] = temp[j].replace("</h3>", '')
            temp[j] = temp[j].replace("<li>", '')
            temp[j] = temp[j].replace("</li>", '')
    return l

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
        # tree = ET.parse("XML_file/{}.xml".format(message.from_user.id))
        # root = tree.getroot()
        # anime_list_comp = []
        # for i in range(len(root) - 1):
        #     if root[i + 1][12].text == "Completed":
        #         anime_list_comp.append(root[i + 1][1].text)
        # r_idx_c = random.randint(0, len(anime_list_comp)-1)
        # bot.send_message(message.from_user.id, anime_list_comp[r_idx_c])
        xml_arr = os.listdir("XML_file")
        html_arr = os.listdir("HTML_file")

        user_id = message.from_user.id
        if "{}.xml".format(user_id) in xml_arr:
            tree = ET.parse("XML_file/{}.xml".format(user_id))
            root = tree.getroot()
            anime_list_completed = []
            for i in range(len(root) - 1):
                if root[i + 1][12].text == "Completed":
                    anime_list_completed.append(root[i + 1][1].text)
            r_idx_c = random.randint(0, len(anime_list_completed) - 1)
            # print(anime_list_plan[r_idx_p])
            bot.send_message(message.from_user.id, anime_list_completed[r_idx_c])

        elif "{}.html".format(user_id) in html_arr:
            completed_arr = table_anime_html(user_id)
            for i in range(len(completed_arr)):
                if completed_arr[i][0] == "Просмотрено":
                    temp = completed_arr[i][1:]
                    r_idx_c = random.randint(0, len(temp) - 1)
                    bot.send_message(message.from_user.id, temp[r_idx_c])

    except FileNotFoundError as f:
        bot.send_message(message.from_user.id, "Для начала пришли твой файл!")
    except ValueError as v:
        bot.send_message(message.from_user.id, "Похоже у тебя нет аниме в этой категории.")


'''@bot.message_handler(commands=['completedhtml'])
def get_random_anime_completed_html(message):
    try:
        completed_arr = table_anime_html(message.from_user.id)
        for i in range(len(completed_arr)):
            if completed_arr[i][0] == "Просмотрено":
                temp = completed_arr[i][1:]
                r_idx_c = random.randint(0, len(temp) - 1)
                # print(temp[r_idx_c])
                bot.send_message(message.from_user.id, temp[r_idx_c])
    # except FileNotFoundError as f:
    #     bot.send_message(message.from_user.id, "Для начала пришли твой файл!")
    except ValueError as v:
        bot.send_message(message.from_user.id, "Похоже у тебя нет аниме в этой категории.")'''

@bot.message_handler(commands=['watching'])
def get_random_anime_watching(message):
    try:
        # # temp = os.listdir(path="XML_file")
        # tree = ET.parse("XML_file/{}.xml".format(message.from_user.id))
        # root = tree.getroot()
        # anime_list_watching = []
        # for i in range(len(root) - 1):
        #     if root[i + 1][12].text == "Watching":
        #         anime_list_watching.append(root[i + 1][1].text)
        # r_idx_w = random.randint(0, len(anime_list_watching)-1)
        # # print(anime_list[r_idx])
        # bot.send_message(message.from_user.id, anime_list_watching[r_idx_w])
        xml_arr = os.listdir("XML_file")
        html_arr = os.listdir("HTML_file")

        user_id = message.from_user.id
        if "{}.xml".format(user_id) in xml_arr:
            tree = ET.parse("XML_file/{}.xml".format(user_id))
            root = tree.getroot()
            anime_list_watching = []
            for i in range(len(root) - 1):
                if root[i + 1][12].text == "Watching":
                    anime_list_watching.append(root[i + 1][1].text)
            r_idx_w = random.randint(0, len(anime_list_watching) - 1)
            # print(anime_list_plan[r_idx_p])
            bot.send_message(message.from_user.id, anime_list_watching[r_idx_w])

        elif "{}.html".format(user_id) in html_arr:
            watching_arr = table_anime_html(user_id)
            for i in range(len(watching_arr)):
                if watching_arr[i][0] == "Смотрю":
                    temp = watching_arr[i][1:]
                    r_idx_w = random.randint(0, len(temp) - 1)
                    bot.send_message(message.from_user.id, temp[r_idx_w])
    except FileNotFoundError as f:
        bot.send_message(message.from_user.id, "Для начала пришли твой файл!")
    except ValueError as v:
        bot.send_message(message.from_user.id, "Похоже у тебя нет аниме в этой категории.")


'''@bot.message_handler(commands=['watchinghtml'])
def get_random_anime_watching_html(message):
    try:
        watching_arr = table_anime_html(message.from_user.id)
        for i in range(len(watching_arr)):
            if watching_arr[i][0] == "Смотрю":
                temp = watching_arr[i][1:]
                r_idx_c = random.randint(0, len(temp) - 1)
                # print(temp[r_idx_c])
                bot.send_message(message.from_user.id, temp[r_idx_c])
    # except FileNotFoundError as f:
    #     bot.send_message(message.from_user.id, "Для начала пришли твой файл!")
    except ValueError as v:
        bot.send_message(message.from_user.id, "Похоже у тебя нет аниме в этой категории.")'''


@bot.message_handler(commands=['plan'])
def get_random_anime_plan(message):
    try:
        # # temp = os.listdir(path="XML_file")
        # tree = ET.parse("XML_file/{}.xml".format(message.from_user.id))
        # root = tree.getroot()
        # anime_list_plan = []
        # for i in range(len(root) - 1):
        #     if root[i + 1][12].text == "Plan to Watch":
        #         anime_list_plan.append(root[i + 1][1].text)
        # r_idx_p = random.randint(0, len(anime_list_plan)-1)
        # # print(anime_list[r_idx])
        # bot.send_message(message.from_user.id, anime_list_plan[r_idx_p])
        xml_arr = os.listdir("XML_file")
        html_arr = os.listdir("HTML_file")

        user_id = message.from_user.id
        if "{}.xml".format(user_id) in xml_arr:
            tree = ET.parse("XML_file/{}.xml".format(user_id))
            root = tree.getroot()
            anime_list_plan = []
            for i in range(len(root) - 1):
                if root[i + 1][12].text == "Plan to Watch":
                    anime_list_plan.append(root[i + 1][1].text)
            r_idx_p = random.randint(0, len(anime_list_plan) - 1)
            # print(anime_list_plan[r_idx_p])
            bot.send_message(message.from_user.id, anime_list_plan[r_idx_p])

        elif "{}.html".format(user_id) in html_arr:
            plan_arr = table_anime_html(user_id)
            for i in range(len(plan_arr)):
                if plan_arr[i][0] == "Буду смотреть":
                    temp = plan_arr[i][1:]
                    r_idx_p = random.randint(0, len(temp) - 1)
                    bot.send_message(message.from_user.id, temp[r_idx_p])
    except FileNotFoundError as f:
        bot.send_message(message.from_user.id, "Для начала пришли твой файл!")
    except ValueError as v:
        bot.send_message(message.from_user.id, "Похоже у тебя нет аниме в этой категории.")


'''@bot.message_handler(commands=['planhtml'])
def get_random_anime_plan_html(message):
    try:
        plan_arr = table_anime_html(message.from_user.id)
        for i in range(len(plan_arr)):
            if plan_arr[i][0] == "Буду смотреть":
                temp = plan_arr[i][1:]
                r_idx_c = random.randint(0, len(temp) - 1)
                # print(temp[r_idx_c])
                bot.send_message(message.from_user.id, temp[r_idx_c])
    # except FileNotFoundError as f:
    #     bot.send_message(message.from_user.id, "Для начала пришли твой файл!")
    except ValueError as v:
        bot.send_message(message.from_user.id, "Похоже у тебя нет аниме в этой категории.")'''

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f'Я бот для рандомизации вашего аниме листа. Приятно познакомиться, {message.from_user.first_name}')
    bot.send_message(message.from_user.id, 'Для начала работы пришли мне свой аниме лист в формате .xml или .html')


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

        if file_extension == ".xml":
            src = 'XML_file/' + "{}.xml".format(message.from_user.id)
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
                # bot.reply_to(message, "{}".format(message.document.file_name))
            bot.reply_to(message, "Пожалуй, я сохраню это")
            html_arr = os.listdir(path="HTML_file")
            if "{}.html".format(message.from_user.id) in html_arr:
                os.remove("HTML_file/{}.html".format(message.from_user.id))
        elif file_extension == ".html":
            src = 'HTML_file/' + "{}.html".format(message.from_user.id)
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
                # bot.reply_to(message, "{}".format(message.document.file_name))
            bot.reply_to(message, "Пожалуй, я сохраню это")
            xml_arr = os.listdir(path="XML_file")
            if "{}.xml".format(message.from_user.id) in xml_arr:
                os.remove("XML_file/{}.xml".format(message.from_user.id))
        else:
            bot.reply_to(message, "Сорри, но это не тот формат")

    except Exception as e:
        bot.reply_to(message, e)

bot.polling(none_stop=True)
