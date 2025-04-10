#5-17
def sum_range(n1, n2):
    return sum(range(n1, n2 + 1))

result1 = sum_range(10, 20)
result2 = sum_range(40, 100)

print("{}에서 {}까지의 합: {}".format(10, 20, result1))
print("{}에서 {}까지의 합: {}".format(40, 100, result2))

#5-21
def 주민번호_rrn(rrn):
    year = int(rrn[:2])
    month = int(rrn[2:4])
    day = int(rrn[4:6])
    
    if year >= 50:
        year += 1900
    else:
        year += 2000

    return "{}년 {}월 {}일".format(year, month, day)

user_input = input("주민번호 앞 6자리를 입력하셈: ")
print(주민번호_rrn(user_input))
