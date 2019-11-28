#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    #네이버웹툰 > 연애혁명 제목 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=570503")
    soup = BeautifulSoup(data, "lxml")
    data.close()
    html = "<html><head><meta charset='utf-8'></haed><body>"
    cartoon_titles = soup.find_all("td", attrs={"class":"title"}) #<td class = "title">...</td>
    for cartoon_title in cartoon_titles :
    #for cartoon_title in cartoon_titles(:2) :
        #print(cartoon_title)
        #리스트에다가 하나씩 넣었다가 넣은 것을 하나씩 출력
        title = cartoon_title.find("a").text
        link = cartoon_title.find("a").get("href")              #태그의 속성값 가져오기. <a href="">text</a>
        link = "https://comic.naver.com" + link
        print(title)
        print(link)
        html += "<a href='{}'>{}</a><br>".format(link, title)     #<a href='link'>title</a>
    html += "</body></html>"

    outputSoup = BeautifulSoup(html, "lxml")        #내가 생성한 html 문자열을 soup 객체로 만들
    prettyHtml = str(outputSoup.prettify())         #예쁘게 html 코드로 만들자

    with open("연애혁명.html", "w", encoding="utf-8") as f :    #html 파일을 만들자
        f.write(prettyHtml)