import os
import leaf
import xml.etree.ElementTree as ET
'''path = "test_dir"
files = os.listdir(path)
files = [os.path.join(path, file) for file in files]
files = [file for file in files if os.path.isfile(file)]
res = max(files, key=os.path.getctime)
print(res)
filename, file_extension = os.path.splitext(str(res))'''
# from bs4 import BeautifulSoup
# import codecs
# fileObj = codecs.open("HTML_file\html.html", "r", "utf_8_sig" )
# contents = fileObj.read()
# soup = BeautifulSoup(contents, 'lxml')
# print(soup.find_all('h3'))
# import lxml.html
# from tabulate import tabulate
# import urllib.request
# fname = r"HTML_file\html.html"
# HtmlFile = open(fname, 'r', encoding='utf-8')
# source_code = HtmlFile.read()
# # print(source_code)
# markup = lxml.html.fromstring(source_code)
#
# tbl = []
# rows = markup.cssselect("tr")
# for row in rows:
#   tbl.append(list())
#   for td in row.cssselect("td"):
#     tbl[-1].append((td.text_content()))
# for i in range(len(tbl)):
#     for j in range(len(tbl[i])):
#         tbl[i][j] = tbl[i][j].strip().replace("\n",'')
# print(tbl)

import bs4
import random
from tabulate import tabulate


def table_anime():
    fname = "HTML_file_test/html.html"
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

lis = table_anime()
print(tabulate(lis))
for i in range(len(lis)):
    if lis[i][0] == "Брошено":
        temp = lis[i][1:]
        r_idx_c = random.randint(0, len(temp)-1)
        print(temp[r_idx_c])
# res = str(q1[0]).split("\n")
# # print(res)
# res.remove(res[0])
# res.remove(res[-1])
# for i in res:
#     if i == '<ul>':
#         res.remove(i)
#     if i == '</ul>':
#         res.remove(i)
# # print(res)
# # for i in range(len(res)):
# #     res[i] = res[i].replace("<h3>", '')
# #     res[i] = res[i].replace("</h3>", '')
# #     res[i] = res[i].replace("<li>", '')
# #     res[i] = res[i].replace("</li>", '')
# # print(res)
# # print('')
# d = dict.fromkeys([res[0]], res[1:])
# # print(d)
# # print(d.get("Смотрю"))