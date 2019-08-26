import time
import random

class User:

    _rice = ['쌀밥', '잡곡밥', '현미밥', '참치덮밥', '김치볶음밥']
    _main_menu = ['카레덮밥', '돼지두루치기', '돼지불고기', '찹스테이크', '골뱅이무침', '마파두부',
                '오징어볶음', '양배추쌈', '훈제오리부추무침', '베이컨야채볶음', '제육볶음', '오징어간장볶음']
    _side_menu = ['어묵볶음', '멸치볶음', '깻잎김치', '도토리묵', '계란장조림', '돼지고기장조림', '무생채나물',
                '두부무침', '계란말이', '취나물된장무침', '소시지야채볶음', '돌나무무침&오징어숙회', '고구마맛탕',
                '아몬드&호두조림']
    _soup = ['고추장찌개', '묵은지감자탕', '김치콩나물국', '미역국', '맑은오징어국', '콩나물국',
            '소고기무국', '시금치된장국', '고사리들깨탕', '돼지김치찌개', '계란국', '동태찌개']

    def allergy_exclude(self, number, allergy) :

        for i in range(0, allergy, 1) :

            if number[i] == 1 :
                self._side_menu.remove('아몬드&호두조림')
                print("견과류", end = "  ")
            elif number[i] == 2 :
                print("우유", end = "  ")
            elif number[i] == 3 :
                self._main_menu.remove('골뱅이무침')
                self._main_menu.remove('오징어볶음')
                self._main_menu.remove('오징어간장볶음')
                self._side_menu.remove('돌나무무침&오징어숙회')
                self._soup.remove('미역국')
                self._soup.remove('맑은오징어국')
                print("해산물", end = "  ")
            elif number[i] == 4 :
                self._main_menu.remove('마파두부')
                self._side_menu.remove('두부무침')
                print("대두", end = "  ")
            elif number[i] == 5 :
                self._side_menu.remove('계란장조림')
                self._side_menu.remove('계란말이')
                print("계란", end = "  ")
            elif number[i] == 6 :
                self._rice.remove('참치덮밥')
                self._side_menu.remove('어묵볶음')
                self._side_menu.remove('멸치볶음')
                print("생선", end = "  ")
            elif number[i] == 7 :
                self._main_menu.remove('돼지두루치기')
                self._main_menu.remove('돼지불고기')
                self._main_menu.remove('찹스테이크')
                self._main_menu.remove('훈제오리부추무침')
                self._main_menu.remove('베이컨야채볶음')
                self._main_menu.remove('제육볶음')
                self._side_menu.remove('돼지고기장조림')
                self._side_menu.remove('소시지야채볶음')
                self._soup.remove('묵은지감자탕')
                self._soup.remove('소고기무국')
                self._soup.remove('돼지김치찌개')
                print("육류", end = "  ")

        print("(이)가 식단표에서 제외되었습니다.")

    def main(self) : 
        print("오늘은 뭐 먹지?\n")
        time.sleep(1)
        start = int(input("식단을 제공받고 싶지 않으시다면 1번을 제공받고 싶으시다면 그 외에 숫자를 입력해주세요 : "))
        if start == 2 :
            print("오늘은 뭐 먹지? 를 방문해주셔서 감사합니다~!")
        elif start == 1 :
            name = input("이름이 뭐예요? ")
            print("\n")
            print("지금부터 간단한 " + name + "님 파악을 할거예요! 성실하게 답변해주세요!")
            time.sleep(1)
            count = int(input(name + "님이 한 끼당 제공받고 싶은 반찬의 개수를 입력해주세요 : "))
            print("")
            print("")
            print(name + "님이 알레르기 있는 음식을 골라주세요!!")
            time.sleep(1)
            print("1.견과류 2.우유 3.해산물 4.대두 5.계란 6.생선 7.육류 : ")
            time.sleep(1)
            allergy = int(input("알레르기 있는 음식이 몇 개입니까? "))
            
            number = []

            for a in range(allergy) :
                allergy_num = int(input("알레르기인 번호를 입력해주세요 : "))
                number.insert(a, allergy_num)

            print("")
            print(".  ", end=''),
            time.sleep(1)
            print(".  ", end=''),
            time.sleep(1)
            print(".  ", end=''),
            time.sleep(1)
            print(".  ", end=''),
            print("분 석 중 . . . . ")
        
            self.allergy_exclude(number, allergy)
        
            print()
            print()

            print("오늘의 식단표")

            rice_len = len(self._rice)
            rice_ran = random.randrange(0, rice_len)
            print("밥 : ", self._rice[rice_ran])

            main_len = len(self._main_menu)
            main_ran = random.randrange(0, main_len)
            print("주메뉴 : ", self._main_menu[main_ran])

            side_len = len(self._side_menu)
            side1 = []
            side2 = [0 for s in range(count)]

            for i in range(0, len(side2)) :
                side2[i] = random.randrange(0, side_len)
                for j in range(0, i) :
                    if side2[i] == side2[j] :
                        i-=1
                        break

            for i in range(0, len(side2)) :
                way = side2[i]
                side1.append(self._side_menu[way])
                print("사이드메뉴 : ", self._side_menu[i])

            soup_len = len(self._soup)
            soup_ran = random.randrange(0, soup_len)
            print("국 : ", self._soup[soup_ran])
    
u = User()
u.main()