from order import Order

from file_IO import FileIO

file_IO = FileIO("file.bin")

history = []
try :
    history = file_IO.load()
except FileNotFoundError :
    print("내역이 없습니다")
print("--------------------------")

o = Order()
o.order_drink()
o.order_price()

file_IO.save(o.order_menu)