# dan = 2

# print(dan, " X ", 1, " = ", dan*1)
# print(dan, " X ", 2, " = ", dan*2)
# print(dan, " X ", 3, " = ", dan*3)
# print(dan, " X ", 4, " = ", dan*4)
# print(dan, " X ", 5, " = ", dan*5)
# print(dan, " X ", 6, " = ", dan*6)
# print(dan, " X ", 7, " = ", dan*7)
# print(dan, " X ", 8, " = ", dan*8)
# print(dan, " X ", 9, " = ", dan*9)



# for i in range(1, 9+1) :
#     print(dan, " X ", i, " = ", dan*i)


# for i in range(1, 9+1) :
#     print(2, " X ", i, " = ", 2*i)
# for i in range(1, 9+1) :
#     print(3, " X ", i, " = ", 3*i)
# for i in range(1, 9+1) :
#     print(4, " X ", i, " = ", 4*i)
# for i in range(1, 9+1) :
#     print(5, " X ", i, " = ", 5*i)
# for i in range(1, 9+1) :
#     print(6, " X ", i, " = ", 6*i)
# for i in range(1, 9+1) :
#     print(7, " X ", i, " = ", 7*i)
# for i in range(1, 9+1) :
#     print(8, " X ", i, " = ", 8*i)
# for i in range(1, 9+1) :
#     print(9, " X ", i, " = ", 9*i)


for dan in range(2, 9+1) :
    for i in range(1, 9+1) :
        if i > 7 :
            break
        if i % 2 == 0 :
            continue
        print(dan, " X ", i, " = ", dan*i)
    print("----------------")