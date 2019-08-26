# number = (input("학번을 입력하세요 : "))

# if number[0:2] == "11" :
#     print("뉴미디어소프트웨어과")
# elif number[0:2] == "12" :
#     print("뉴미디어소프트웨어과")
# elif number[0:2] == "13" :
#     print("뉴미디어웹솔루션과")
# elif number[0:2] == "14" :
#     print("뉴미디어웹솔루션과")
# elif number[0:2] == "15" :
#     print("뉴미디어디자인과")
# elif number[0:2] == "16" :
#     print("뉴미디어디자인과")
# elif number[0:2] == "21" :
#     print("뉴미디어소프트웨어과")
# elif number[0:2] == "22" :
#     print("뉴미디어소프트웨어과")
# elif number[0:2] == "23" :
#     print("뉴미디어웹솔루션과")
# elif number[0:2] == "24" :
#     print("뉴미디어웹솔루션과")
# elif number[0:2] == "25" :
#     print("뉴미디어디자인과")
# elif number[0:2] == "26" :
#     print("뉴미디어디자인과")
# elif number[0:2] == "31" :
#     print("인터랙티브미디어과")
# elif number[0:2] == "32" :
#     print("인터랙티브미디어과")
# elif number[0:2] == "33" :
#     print("뉴미디어디자인과")
# elif number[0:2] == "34" :
#     print("뉴미디어디자인과")
# elif number[0:2] == "35" :
#     print("뉴미디어솔루션과")
# elif number[0:2] == "36" :
#     print("뉴미디어솔루션과")

# 선생님 답안
# student_number = (input("학번을 입력하세요 : "))

# grade = student_number[0]
# classroom = student_number[1]

# if grade == "1" or grade == "2" :
#     if classroom == "1" or classroom == "2" :
#         print("뉴미디어소프트웨어과")
#     elif classroom == "3" or classroom == "4"  :
#         print("뉴미디어웹솔루션과")
#     elif classroom == "5" or classroom == "6" :
#         print("뉴미디어디자인과")
# elif grade == "3" :
#     if classroom == "1" or classroom == "2" :
#         print("인터랙티브미디어과")
#     elif classroom == "3" or classroom == "4"  :
#         print("뉴미디어디자인과")
#     elif classroom == "5" or classroom == "6" :
#         print("뉴미디어솔루션과") 

majors = [
    ["뉴미디어 소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
    ["뉴미디어 소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
     ["인터랙티브미디어","뉴미디어디자인과","뉴미디어솔루션"]
    ]
    
student_number = input("학번을 입력하세요")

grade = student_number[0]
grade = int(grade)
classroom = student_number[1]
classroom = int(classroom)

print(majors[grade-1][(classroom-1)//2])
