name = ""
gender = ""
age = 0

# print(name, len(name), age - 10)

name = input("이름을 입력하세요 : ")
gender = input("성별을 입력하시오(남/여 둘 중 하나만 골라)")
age = input ("나이를 입력하세요 : ")

if gender == "남":
    gender=" Mr."
elif gender == "여":
    gender = "Ms."
print(f"{gender}{name[0]}님 반갑습니다. 지옥에 오신것을 환영합니다!")

if int(age) <= 18:
    print("당신은 미성년자시군요 미성년자 전용 건전한 지옥으로 입장하세요.")
elif int(age) >= 19:
    print("당신은 성인이시군요. 성인용 레알살벌한 지옥으로 입장하세요.")
