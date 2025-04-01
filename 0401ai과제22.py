n_list = [10,20,30,50,60]
min_value = n_list[0]
for num in n_list:
    if num < min_value:
        min_value = num

        
print("리스트에서 가장 작은 값:", min_value)


n_list = [int(input(f"{i+1}번째 정수를 입력하세요: ")) for i in range(5)]


total = sum(n_list)
average = total / len(n_list) 
max_value = max(n_list) 
min_value = min(n_list)  


print("\n입력된 값:", n_list)
print(f"합: {total}")
print(f"평균: {average:.2f}")  
print(f"최댓값: {max_value}")
print(f"최솟값: {min_value}")

import math 


n = int(input("입력할 숫자의 개수를 입력하세요: "))
numbers = [float(input(f"{i+1}번째 숫자를 입력하세요: ")) for i in range(n)]


mean = sum(numbers) / n


variance = sum((x - mean) ** 2 for x in numbers) / n
std_dev = math.sqrt(variance)


print("\n입력된 값:", numbers)
print(f"평균: {mean:.2f}")
print(f"표준편차: {std_dev:.2f}")
