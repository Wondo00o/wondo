Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(1, 10):
    print(f"2 x {i} = {2 * i}")

    
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
>>> i = 1
>>> while i < 10:
...     print(f"2 x {i} = {2 * i}")
...     i += 1
... 
...     
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
>>> 
>>> for i in range(3):
...     print('Python')
...     print('is')
...     print('Fun!')
... 
...     
Python
is
Fun!
Python
is
Fun!
Python
is
Fun!
>>> 
>>> while (c := input("b, c, p 중 선택: ")) not in "bcp":
...     print("메뉴를 다시 입력하세요.")
... 
...     
b, c, p 중 선택: d
메뉴를 다시 입력하세요.
