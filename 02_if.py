# ja = ""
# n1 = 0
# n2 = 0
# result = 0

# while True:
#     ja = input("무슨 계산할래? 기호로만 적어(+, -, *, /)")
#     n1 = int(input("첫번째 숫자를 말해롸"))
#     n2 = int(input("두번째 숫자를 말해롸"))
#     if ja == "+":
#         result = n1 + n2
#     elif ja == "-":
#         result = n1 - n2
#     elif ja == "*":
#         result = n1 * n2
#     elif ja == "/":
#         result = n1 / n2
#     else:
#         print("아진짜 잘 입력해롸 첨부터")
#         continue
#     print(f"{n1} {ja} {n2} = {result}")

#똑똑한계산귀\
gyeasan = ""
result = 0
running = True
show = True

while running   :
    gyeasan = input("계산기입니다 물어보쉐요 : ")
        if "+" in gyeasan:
            result = int(gyeasan.split("+")[0]) + int(gyeasan.split("+")[1])
        elif "-" in gyeasan:
            result = int(gyeasan.split("-")[0]) - int(gyeasan.split("-")[1])
        elif "*" in gyeasan:
            result = int(gyeasan.split("*")[0]) * int(gyeasan.split("*")[1])
        elif "/" in gyeasan:
            result = int(gyeasan.split("/")[0]) / int(gyeasan.split("/")[1])
        elif "q" in gyeasan:
            print("계산기를 종료함니돠 주인님 바이봐이")
            running = False
            show = False
        else:
            print("연산식이 잘못됨 다쉬")
            show = False
        if show:
        print(f"{gyeasan} = {result}")






