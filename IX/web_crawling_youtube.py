
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__' :
    url = "https://www.youtube.com/channel/UCW_WhXrfK3uPgljcdjFbsbg/videos"
    with requests.post(url) as response :
        soup = BeautifulSoup(response.text, "lxml")

    #youtube_titles = soup.find_all("a", attrs={"class":"yt-uix-tile-link"})
    youtube_titles = soup.select("a.yt-uix-tile-link")  #<a class="yt-uix-tile-link"></a>
    for youtube_title in youtube_titles:
        print(youtube_title.text)