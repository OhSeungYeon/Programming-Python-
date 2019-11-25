from order import Order

from file_IO import FileIO

file_IO = FileIO("file.txt")

history = []
try :
    history = file_IO.read()
    print(history)

except FileNotFoundError :
    print("내역이 없습니다")
print("--------------------------")

o = Order()
o.order_drink()
o.order_price()

for i in o.order_menu:
    file_IO.append(str(i))
