from drink import Drink
from cuprice import CupRice
from cupnoodle import CupNoodle
from cupbulgogirice import CupBulgogiRice
from tunamayo import TunaMayo
from meatmayo import MeatMayo


class Order:
    def __init__(self):
        self.order_menu = []

    def show_menu(self):
        print("0:컵라이스 3500원, 1:컵누들 3500원, \t"
              "2:컵불고기라이스 4000원, 3:참치마요 4000원, 4:고기마요 4000원")

    def order_drink(self):
        while True:
            self.show_menu()
            order = input("어떤 메뉴를 선택하시겠습니까?")
            if order == "":
                break
            if int(order) == 0:
                drink = CupRice("컵라이스", 3500)
                menu = "컵라이스"
            elif int(order) == 1:
                drink = CupNoodle("컵누들", 3500)
                menu = "컵누들"
            elif int(order) == 2:
                drink = CupBulgogiRice("컵불고기라이스", 4000)
                menu = "컵불고기라이스"
            elif int(order) == 3:
                drink = TunaMayo("참치마요", 4000)
                menu = "참치마요"
            elif int(order) == 4:
                drink = MeatMayo("고기마요", 4000)
                menu = "고기마요"

            drink = Drink(menu, 0)
            drink.order()
            self.order_menu.append(drink)

        for i in self.order_menu:
            print(i)
        print("총금액: " + str(self.order_price()) + "원")

    def order_price(self):
        total = 0
        for i in self.order_menu:
            total += i.price

        return total

