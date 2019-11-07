
class Drink :

    _drinks = ["없음", "콜라", "사이다", "환타(오렌지)", "환타(포도)", "마운틴듀"]

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.drink = 0

    def set_drink(self):
        self.drink = input(
            "원하는 음료수를 선택해주세요(0:안먹어, 1:콜라, 2:사이다, 3:환타(오렌지), 4:환타(포도), 5:마운틴듀)")
        if self.drink == "" :
            self.drink = 0
        else :
            self.drink = int(self.drink)

        if (self.drink == 1) | (self.drink == 2) | (self.drink == 3) | (self.drink == 4) | (self.drink == 5):
            self.price += 500

    #def set_price(self):

        #o = Order

        #if (o.order == "컵라이스") | (o.order == "컵누들") :
            #self.price += 3500

        #else :
          #self.price += 4000

    def __str__(self):
        return "메뉴:" + self.name + "\t" + \
               "\t" + "가격:" + str(self.price) + "\t" + "음료수" + str(self.drink)
    #+ "매운맛:" + self.spicy +

    def order(self):
        self.set_drink()
