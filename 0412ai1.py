#8-5
import math

print("각도 |   sin   |   cos   |   tan")
print("-------------------------------")

for degree in range(0, 181, 10):
    rad = math.radians(degree)
    sin_val = round(math.sin(rad), 4)
    cos_val = round(math.cos(rad), 4)
    
    if degree == 90:
        tan_val = "무한"
    else:
        tan_val = round(math.tan(rad), 4)
    
    print(f"{degree:>3}° | {sin_val:>7} | {cos_val:>7} | {tan_val}")

#8-9
import random


x = random.randint(1, 20)
n = 0  

while True:
    guess = int(input("숫자를 입력하세요 (1~20): "))
    n += 1

    if guess < x:
        print("입력한 숫자가 정답보다 작습니다.")
    elif guess > x:
        print("입력한 숫자가 정답보다 큽니다.")
    else:
        print("정답입니다!")
        break


if n <= 3:
    print(f"{n}번만에 맞춘 당신은 천재!")
elif n <= 6:
    print(f"{n}번 만에 맞추셨네요 잘하셨어요^^")
else:
    print(f"{n}번 만에 맞추다니...쩝쩝...")
