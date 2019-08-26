#야구게임
#세자리 중복없는 임의의 수 만들자
#무한반복
#사용자 입력을 받자
#strike, ball 판정하다
#사용자 입력한것, strike, ball 출력하자
#임의의 수랑 사용자 입력한게 같으면 HIT, break
import random

#r0 = random.randrange(1, 9+1)
#r0 = str(r0)
#r1 = random.randrange(1, 9+1)
#r1 = str(r1)
#r2 = random.randrange(1, 9+1)
#r2 = str(r2)

l = list(range(1, 9+1))
random.shuffle(l) #[3, 6, 4, 8, 5, 5....]
#l[:3] #364

# a=""
# for i in l[:3] :
#     a+=str(i)

computer = "".join(str(i) for i in l[:3]) # 위에 세줄을 이렇게 한 줄로 표현할 수 있다.
print(computer)

#random.sample(range(1, 9+1), 3) #1~9까지의 숫자중에서 sample 3개를 가져오는 것 중복은 당연히 안된다.

#computer = str(random.randrange(100, 999+1)) --> 이렇게 하면 숫자가 중복이 될 수도 있음

while True :
    
    player = input("숫자 세자리 맞춰봐~ : ")

    strike = 0
    ball = 0

    #strike, ball 판정하자
    for i in range(len(computer)) :
        for j in range(len(player)) :
            if computer[i] == player[j] :
                if i==j :
                    strike += i
                else :
                    ball += i

    #print(player, "strike : ", strike, "ball : ", ball)
    print("{}\tstrike:{}\tball:{}", player, strike, ball)
    if computer == player :
        print("HIT")
        break