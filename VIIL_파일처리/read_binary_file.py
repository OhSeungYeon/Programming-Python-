f = open("data.bin", "wb")

data = f.read()
print(data)
for item in data :
    print(item)
f.close()