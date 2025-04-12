#9-5

with open("number1to10.txt", "w") as file:
    for i in range(1, 11):
        file.write(f"{i}\n")

#9-9

with open("coord.txt", "w") as file:
    file.write("8\n")
    file.write("6 10\n")
    file.write("2 4\n")
    file.write("6 2\n")
    file.write("5 2\n")
    file.write("4 8\n")
    file.write("6 7\n")
    file.write("1 1\n")
    file.write("8 3\n")


with open("coord.txt", "r") as file:
    lines = file.readlines()


n = int(lines[0].strip())


points = []
for line in lines[1:n+1]:
    x, y = map(int, line.strip().split())
    points.append((x, y))


points.sort(key=lambda point: (point[0], point[1]))


for point in points:
    print(point)
