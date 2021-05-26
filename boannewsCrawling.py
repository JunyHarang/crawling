from re import I
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.boannews.com/media/t_list.asp')
soup = BeautifulSoup(response, 'html.parser')

idex_num = 1

f = open("/bitcamp/파이썬/source_visual/practice/보안뉴스.txt", 'w')

for span in soup.select("div.news_list"):
    data = ('='*100 + "\n")
    data += (str(idex_num) + "번째" + span.get_text()) + "\n"
    idex_num += 1
    f.write(data)
f.close()
