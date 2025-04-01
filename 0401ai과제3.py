#15
greet = 'Have a beautiful Day'

print(greet[0:4])
print(greet[7:16])
print(greet[-3:])

#17
animals = ["dog", "cat", "tiger", "lion"]
animals.append(animals.pop(0))
print(animals)
for animal in animals:
    print(f"I love {animal}")

animals = ["dog", "cat", "tiger", "lion"]


animals.append(animals.pop(0))


for animal in animals:
    print(f"I love {animal}")

#19
s_list = ['abc', 'bcd', 'abc', 'abba', 'cddc', 'opq', 'opq']
new_s_list = []

for item in s_list:
    if item not in new_s_list: 
        new_s_list.append(item)

print(new_s_list)

#21
compressed = "a2b3c6a2c3f1g1" 
decompressed = "" 

for i in range(0, len(compressed), 2):
    char = compressed[i]  
    count = int(compressed[i + 1]) 
    decompressed += char * count 

print(decompressed)

#23

person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평강', 22, 0, 169.0, 60.0]
person4 = ['혁거세', 40, 1, 150.0, 50.0]


person_list = [person1, person2, person3, person4]


def how_many_persons(person_list):
    return len(person_list)  


print("총 인원 수:", how_many_persons(person_list))



