"""def anagrams(s: str, list: list) -> list:
    letters_in_s = set([x for x in s])
    anagrams_words = []
    for i in list:
        letters_in_i = set([x for x in i])
        if letters_in_i == letters_in_s:
            anagrams_words.append(i)
    return anagrams_words


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy', 'lacer']))"""

import re
import ssl
import urllib
from urllib import request
import csv

ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url="https://quke.ru/shop/smartfony/apple?page-size=72", headers=headers)
adres_request = urllib.request.urlopen(req).read().decode()
pattern = r"(?:onerror=\"this\.onerror=null;this\.src='/assets/img/no-photo-with-cat\.png';\"[\s]+title=\")(?P<phones>[^\"]+)(?:[^Ц]+)(?:Цена</span>[\n\s]+<span class=\"b-card2-v2__price-val\">)(?P<prices>[^\<]+)"
matches = re.findall(pattern, adres_request)
d = {}
for i in range(len(matches)):
    if len((matches[i][1])) == 6:
        d[matches[i][0]] = int((matches[i][1][0:2] + matches[i][1][3:6]))
    elif len((matches[i][1])) == 7:
        d[matches[i][0]] = int((matches[i][1][0:3] + matches[i][1][4:7]))
print(f"Самый дорогой телефон: {max(d, key=d.get)}, Его цена: {max(d.values())}")
print(f"Самый дешёвый телефон: {min(d, key=d.get)}, Его цена: {min(d.values())}")
print(f"Средняя стоимость телефонов: {sum(d.values()) / len(d)}")
with open('Smartphones.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Название смартфона', 'Цена в рублях'])
    for match in matches:
        match = list(match)
        filter_match = [match[j] for j in range(len(match)) if len(match[j].split()) != 0]
        writer.writerow(filter_match)

# 72 айфона
