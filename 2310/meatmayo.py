from drink import Drink

class MeatMayo(Drink):
  _spicys = ["순한맛", "1단계", "2단계", "3단계", "4단계", "5단계"]

  def __init__(self, name, price):
    super().__init__(name, price)
    self.spicy = -1

  def set_spicy(self):
      if self.spicy == -1 :
        self.spicy = "없음"

  def __str__(self):
    return super().__str__() + "\t매운맛:" + MeatMayo._spicys[self.spicy]

  def order(self):
    super().order
    self.set_spicy()