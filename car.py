class Car :

    count = 0  #car.count 쓰면 안 됨

    def __init__(self, type, speed) :
        self.type = type
        self.speed = speed
        Car.count += 1  #count만 쓰면 안 됨

    @classmethod         #반드시 있어야 함
    def get_count(cls) : #꼭 이름이 cls가 아니여도 됨
        return cls.count  #Car.count도 가능

    def move(self) :
        print(self.type + "(이)가 " + str(self.speed) + " 속도로 움직입니다.")

    def speed_up(self, amount) :
        self.speed += amount #그냥 speed 쓰면 안 됨

    def speed_down(self, amount) :
        self.speed -= amount

print(Car.get_count())
c = Car("스포츠카", 200)

c.speed_up(10)
c.move()
c.speed_down(10)
c.move()

d = Car("모닝", 200)
d.speed_up(50)
d.move()
d.speed_down(150)
d.move()