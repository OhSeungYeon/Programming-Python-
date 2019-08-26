import random
def rolling_dice1() :
    n = random.randint(1,6) #1<=n<=6 랜덤수
    print("6면 주사위 굴린 결과 : ", n)


def rolling_dice2(pip) :
    n = random.randint(1, pip) #1<=n<=pip 랜덤
    print(pip, "면 주사위 굴린 결과 : ", n)

rolling_dice(4)
rolling_dice(6)
rolling_dice(6)
rolling_dice(8)
rolling_dice(10)
rolling_dice(12)
rolling_dice(20)


def rolling_dice(pip, repeat) :
    for r in range(1, repeat+1) :
        n = random.randint(1,pip)
        print(pip, "면 주사위 굴린 결과 : ", r, " : ", n)

rolling_dice(6, 1)
rolling_dice(6, 2)

#109

def star() :
    print("******")

star()  #*****
star()  #*****
star()  #*****

#p113

print("♥")
print("♥", "♪")
print("♥", "♪", "♣")
print("♥", "♪", "♣", "♠")
print("♥", "♪", "♣", "♠", "★")

def p(*args) :o987
    str = ""
    for a in args :
        string += a
    print(string.strip())
p("♥")
p("♥", "♪")
p("♥", "♪", "♣", "♠")


#114
def p1(space, space_num, *args) :
    str = args[0]
    for i in range(1, len(args)) :
        str = str + (space * space_num) + args[i]
    print(str)
p(",", 3, "♥", "♪")
p("★", 2, "♥", "♪", "♣")
p("_", 3, "♥", "♪", "♣", "♠")


#115
def star2(ch, *nums) :
    # for i in range(len(nums)) :
    #     print(ch * nums[i])
    for n in nums :
        print(ch * n)
star2("♪", 3)
star2("♥", 1, 2, 3)

def fn(a, b, c, d, e) :
    print(a, b, c, d, e)
fn(1, 2, 3, 4, 5)
fn(10, 20, 30, 40, 50)
fn(5, 6, 7, 8, 9)
fn(a=1, b=2, c=3, d=4, e=5)
fn(e=5, d=4, c=3, b=2, a=1)
fn(1, 2, c=3, e=5, d=4)
# fn(d=4, e=5, 1, 2, 3) #에러 (키워드가 순서적인 면이 없어서 1, 2, 3을 넣는 순서가 애매해서 에러가 난다.)