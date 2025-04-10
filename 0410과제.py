#5-5
def inch2cm(inch):
    return inch * 2.54
for i in range(1, 6):
    cm = inch2cm(i)
    print(f"{i} inch = {cm:.2f} cm")

#5-9
def mean_of_n(nums):
    return sum(nums) / len(nums)

def maxs_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

numbers = []

print("숫자를 입력하세요. 종료를 원하면 끝 입력.")
while True:
    user_input = input("숫자 입력: ")
    if user_input == '끝':
        break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("유효한 숫자가 아닙니다. 다시 입력해주세요.")

if numbers:
    print(f"평균값: {mean_of_n(numbers):.2f}")
    print(f"최댓값: {maxs_of_n(numbers)}")
    print(f"최솟값: {min_of_n(numbers)}")
else:
    print("입력된 숫자가 없습니다.")
