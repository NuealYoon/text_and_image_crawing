# !/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

# - 홈페이지에 표시되는 부분의 코드를 확인 하기 위해서는 크롬 브라우져에서 개발자 모드 화면 중 'Ctrl + shift + c'를 통해
#   확인 하고자 하는 코드의 위치를 볼 수 있다.

# - 파이썬 문법 with as는 아래와 같은 코드 이다.
# response = urlopen('https://en.wikipedia.org/wiki/Main_Page')

# - 아래 코드는 https://en.wikipedia.org/wiki/Main_Page 에서 beautifulsoup를 활용해 'a'에 있는 href를 찾아 프린트 한다.
# 'href'는 다른 홈페이지에 접속하기 위한 링크를 저장하는 변수 이다.
# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))

##################


from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

response = urlopen('https://www.naver.com/')
soup = BeautifulSoup(response, 'html.parser')
pp=(json.loads(str(soup)))

print(pp['data'])
if False:
        i = 1
        f = open("새파일.txt", 'w')
        for anchor in soup.select("span.ah_k"):
            data = str(i) + "위 : " + anchor.get_text() + "\n"
            i = i + 1
            f.write(data)
        f.close()


##################

from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

response = urlopen('https://www.naver.com/srchrank?frm=main&ag=30s&gr=1&ma=-2&si=0&en=0&sp=0')
soup = BeautifulSoup(response, 'html.parser')
pp=(json.loads(str(soup)))

print(pp['data'])
if False:
        i = 1
        f = open("새파일.txt", 'w')
        for anchor in soup.select("span.ah_k"):
            data = str(i) + "위 : " + anchor.get_text() + "\n"
            i = i + 1
            f.write(data)
        f.close()