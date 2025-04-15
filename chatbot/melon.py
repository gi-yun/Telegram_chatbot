import requests as req
from bs4 import BeautifulSoup as bs
url = "https://www.melon.com/chart/index.htm"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
web = req.get(url, headers = headers)
soup = bs(web.content, 'html.parser')

title = soup.select_one(".wrap_song_info")
atitle =  title.select_one('a')

aname0 =  title.select_one('.checkEllipsis')
aname = aname0.select_one('a')

print(f'1위: {aname0.text}, / {aname.text}')

print()
def melon():
    rtitle = soup.select('.rank01')[:20]
    name = soup.select('.checkEllipsis a')[:20]
    str=''
    for i, (t,n) in enumerate(zip(rtitle,name),1):
        str+=f'{i}위: {t.text.strip()} / {n.text} \n'
    return str