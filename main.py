import xml.etree.ElementTree as ET
import random
import os
temp = os.listdir(path="XML_file")
tree = ET.parse("XML_file/{}".format(temp[0]))
root = tree.getroot()
# print(len(root))
# print(root.tag)
# for child in root:
#     print(child.tag, child.attrib)
anime_list = []
for i in range(len(root)-1):
    if root[i+1][12].text == "Completed":
        anime_list.append(root[i+1][1].text)
r_idx = random.randint(0, len(anime_list))
print(r_idx)
print(anime_list[r_idx])