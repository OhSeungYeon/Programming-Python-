
import pyautogui as pag
import time

if __name__ == '__main__':
    #크롬 이미지 인식하자
    data = pag.locateOnScreen("구글_아이콘3.PNG")
    print(data)
    #가운데 좌표 찾자
    #center = (data.left + (data.width/2), data.top + (data.height/2))
    center = pag.center(data)
    #pag.moveTo(center, duration=2)
    #마우스 이동하자
    #더블클릭하자
    pag.doubleClick(center, duration=2)