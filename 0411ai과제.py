#7-5
t=(10,20,30,40)
print(t[0])
print(t[0:2])
print(t[1:])
print(t[:3])
print(t[1::2])
print(t[::-1])

#7-9
tup = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)
unique_tup = tuple(sorted(set(tup)))
print("중복 제거:", unique_tup)

#7-13
lst = [5, 6, 3, 9, 2, 12, 3, 8, 7]

n = len(lst)

for i in range(n - 1): 
    for j in range(n - 1 - i): 
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(lst)

#7-17-1
population_A = [100, 150, 230, 120, 180, 100, 140, 95, 81, 4]
population_B = [300, 420, 530, 420, 400, 300, 40, 5, 1, 1, 1]

투표_A = sum(population_A[2:])
투표_B = sum(population_B[2:])

print("마을 A와 마을B에 보낼 투표용지의 개수는 각각 {}장과 {}장입니다.".format(투표_A, 투표_B))

#7-17-2

total_A = sum(population_A)
total_B = sum(population_B)


나이_A = sum(population_A[7:])
나이_B = sum(population_B[7:])


고령_A = round(나이_A / total_A, 3)
고령_B = round(나이_B / total_B, 3)

print("마을 A와 B의 고령화 정도는 각각 {}와 {}입니다.".format(고령_A, 고령_B))

