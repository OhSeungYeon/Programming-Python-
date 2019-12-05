
import pyautogui as pag

if __name__ == '__main__' :
    pag.moveTo(42, 430, duration=2)
    #pag.click()
    #pag.click()
    pag.move(100, 200, duration=1)
    #pag.rightClick()
    pag.click(button="right")
    pag.drag(0, 200, duration=2)