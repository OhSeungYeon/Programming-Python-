
from urllib.request import urlopen
import json

if __name__ == '__main__':

    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data :
        j = json.loads(data.read())
    #print(j["data"]["webtoon"]["webtoonEpisodes"][1]["title"])

    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]

    for cartoon_title in cartoon_titles :
        title = cartoon_title["title"]
        print(title)
        thumbnail =cartoon_title
        print(thumbnail)