
import pyautogui as pag
import time

if __name__ == '__main__':
    #메모장 프로그램 실행하자
    pag.moveTo(28, 1072, duration=2)
    pag.click()
    pag.press("hangul")
    pag.typewrite("apah")
    pag.press("enter")
    time.sleep(2)

    # hello world 치자
    pag.moveTo(127, 583, 2)
    pag.click()
    pag.typewrite("hello world")

    # 두번 내리자
    pag.press("enter")
    pag.press("enter")

    # 반갑구나 세상아 치자
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")

    # 저장하자
    pag.hotkey('ctrl', 's')
    time.sleep(1)

    # 파일이름 : 파이썬월드
    pag.typewrite("C:\\Users\\dhtmd")
    pag.press("hangul")
    pag.typewrite("vkdlTjsdnjfem")

