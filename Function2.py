# star("*", 3, "_",2,3)

def star(mark, repeat, space, space_repeat, line) :
    for _ in range(line) : # for 문에 _는 i를 쓰지 않을 때 무의미 해서 _로 지정한다.
        String = (mark*repeat) + (space*space_repeat) + (mark*repeat)
        print(String)
star("*", 3, "_",2,3)

#119
def hello(msg="안녕하세요") :
    print(msg + "!")
hello("오랫만이예요")
hello("이영희")
hello()

#120
def hello2(name, msg="안녕하세요") :
    print(name + "님, " + msg + "!")
hello2("김철수", "오랜만이에요")
hello2("이영희")
#hello2() #에러 name 인자 없음

def fn2(a, b=[]) :
    b.append(a) 
    print(b)
fn2(3)    #[].append(3) => [3]
fn2(5)    #[].append(5) => [5]
fn2(10)
print("\n\n\n")


def gugudan(dan=2) :

    for i in range(2, 10) :
        print(str(dan), "X", str(i), "=", str(dan*i))

gugudan(3)
gugudan(2)
gugudan()

def sum(*numbers) :
    sum_value = 0
    for number in numbers :
        sum_value = sum_value + number
    return sum_value

result = sum(1,3)
print('1 + 3 = ', result)
print("1 + 3 + 5 + 7 =", sum(1,3,5,7))


def min(*numbers) :
    min_value = numbers[0]
    for number in numbers :
        if min_value > number :
            min_value = number
    return min_value

print("최솟값 min(3, 6, -2) =", min(3, 6, -2))


def max(*numbers) :
    max_value = 0
    for number in numbers :
        if max_value < number :
            max_value = number
    return max_value

print("최댓값 max(8, 1, -1, 12) =", max(8, 1, -1, 12))


def multi_num(multi, start, end) :
    result = []
    for n in range(start, end) :
        if n % multi == 0 :
            result.append(n)
    return result
print("multi_num(17, 1, 200) =", multi_num(17, 1, 200)) #17의 배수가 출력 (1~199)
print("multi_num(3, 1, 100) =", multi_num(3, 1, 100)) #3의 배수가 출력(1~99)


def min_max(*args) :
    min = args[0]
    max = args[0]
    for arg in args :
        if min > arg :
            min = arg
        if max < args :
            max = arg
    return min, max #java에서는 두개를 한꺼번에 리턴할 수 없다. (파이썬의 장점)

print(min_max(52, -3, 23, 89, -21))
min_value, max_value = min_max(52, -3, 23, 89, -21)
print("최솟값 : ", min_value)
print("최댓값 : ", max_value)