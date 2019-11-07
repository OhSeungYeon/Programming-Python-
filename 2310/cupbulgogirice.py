from drink import Drink

class CupBulgogiRice(Drink):
  _spicys = ["순한맛", "1단계", "2단계", "3단계", "4단계", "5단계"]

  def __init__(self, name, price):
    super().__init__(name, price)
    self.spicy = 2

  def set_spicy(self):
    self.spicy = input("원하는 매운맛 강도를 선택해주세요(0:순한맛, 1:1단계, 2:2단계, 3:3단계, 4:4단계, 5:5단계)")
    if self.spicy == "":
      self.spicy = 2
    elif self.spicy == 0:
      self.spicy = "순한맛"
    elif self.spicy == 1:
      self.spicy = "1단계"
    elif self.spicy == 2:
      self.spicy = "2단계"
    elif self.spicy == 3:
      self.spicy = "3단계"
    elif self.spicy == 4:
      self.spicy = "4단계"
    elif self.spicy == 5:
      self.spicy = "5단계"

  def __str__(self):
    return super().__str__() + "\t매운맛:" + CupBulgogiRice._spicys[self.spicy]

  def order(self):
    super().order
    self.set_spicy()