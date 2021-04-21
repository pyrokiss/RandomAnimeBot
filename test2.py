import os
import xml.etree.ElementTree as ET
import random
import bs4

id_user = 485359364

def table_anime(id):
    fname = "HTML_file_test/{}.html".format(id)
    HtmlFile = open(fname, 'r', encoding='utf-8')
    source_code = HtmlFile.read()
# print(source_code)
    soup = bs4.BeautifulSoup(source_code,'html.parser')
    q1=soup.find_all('td')
    print(len(q1))
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
            # if j == '</ul>':
            #     temp.remove(j)
    for i in l:
        temp = i
        for j in range(len(temp)):
            temp[j] = temp[j].replace("<h3>", '')
            temp[j] = temp[j].replace("</h3>", '')
            temp[j] = temp[j].replace("<li>", '')
            temp[j] = temp[j].replace("</li>", '')
    return l


# xml_arr = os.listdir("test_dir")
# html_arr = os.listdir("HTML_file_test")

filename, file_extension = os.path.splitext(str("{}.xml".format(id_user)))
# print(file_extension)

if file_extension == ".xml":
    tree = ET.parse("XML_file/{}.xml".format(id_user))
    root = tree.getroot()
    anime_list_plan = []
    for i in range(len(root) - 1):
        if root[i + 1][12].text == "Completed":
            anime_list_plan.append(root[i + 1][1].text)
    r_idx_p = random.randint(0, len(anime_list_plan) - 1)
    print(anime_list_plan[r_idx_p])
    # bot.send_message(message.from_user.id, anime_list_plan[r_idx_p])
elif file_extension == ".html":
    plan_arr = table_anime(id_user)
    for i in range(len(plan_arr)):
        if plan_arr[i][0] == "Просмотрено":
            temp = plan_arr[i][1:]
            r_idx_c = random.randint(0, len(temp) - 1)