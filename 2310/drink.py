class Drink :

    _drinks = ["없음", "콜라", "사이다", "환타(오렌지)", "환타(포도)", "마운틴듀"]

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.drink = 0
        self.spicy = 0

    def get_price(self):
        return self.price

    def set_drink(self):
        self.drink = input(
            "원하는 음료수를 선택해주세요(0:안먹어, 1:콜라, 2:사이다, 3:환타(오렌지), 4:환타(포도), 5:마운틴듀)")
        if self.drink == "" :
            self.drink = 0
        if (int(self.drink) == 1) | (int(self.drink) == 2) | (int(self.drink) == 3) | (int(self.drink) == 4) | (int(self.drink) == 5):
            self.price += 500

        if int(self.drink) == 0 : self.drink = "안먹을래요"
        elif int(self.drink) == 1: self.drink = "콜라"
        elif int(self.drink) == 2 : self.drink = "사이다"
        elif int(self.drink) == 3 : self.drink = "환타(오렌지)"
        elif int(self.drink) == 4 : self.drink = "환타(포도)"
        elif int(self.drink) == 5 : self.drink = "마운틴듀"

    def __str__(self):
        return "메뉴:" + self.name + "\t" + \
               "\t" + "가격:" + str(self.price) + "\t" + "음료수:" + str(self.drink)

    def order(self):
        self.set_drink()
