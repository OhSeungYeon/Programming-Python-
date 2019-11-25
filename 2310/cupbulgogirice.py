from drink import Drink

class CupBulgogiRice(Drink):
  _spicys = ["없음", "순한맛", "1단계", "2단계", "3단계", "4단계", "5단계"]

  def __init__(self, name, price):
    super().__init__(name, price)
    self.spicy = 3

  def set_spicy(self):
    self.spicy = input("원하는 매운맛 강도를 선택해주세요(1:순한맛, 2:1단계, 3:2단계, 4:3단계, 5:4단계, 6:5단계)")
    if self.spicy == "":
      self.spicy = 3

  def __str__(self):
    return super().__str__() + "\t매운맛:" + CupBulgogiRice._spicys[int(self.spicy)]

  def order(self):
    super().order()
    self.set_spicy()