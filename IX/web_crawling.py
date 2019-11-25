#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    #네이버웹툰 > 연애혁명 제목 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=570503")
    soup = BeautifulSoup(data, "lxml")
    cartoon_titles = soup.find_all("td", attrs={"class":"title"})
    for cartoon_title in cartoon_titles :
        #print(cartoon_title)
        #리스트에다가 하나씩 넣었다가 넣은 것을 하나씩 출력
        title = cartoon_title.find("a").text
        print(title)
    