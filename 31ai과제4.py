Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for num in range(100, 1000):
... 
...     a = num // 100
...     b = (num // 10) % 10
...     c = num % 10
...     if num == (a**3 + b**3 + c**3):
...         print(num)
... 
...         
153
370
371
407
>>> fuel = 500
>>> while fuel > 50:
...     action = input(f"현재 연료: {fuel} - 충전(+), 사용(-) 입력: ")
...     if action[0] == '+':
...         fuel += int(action[1:])
... 
...         
현재 연료: 500 - 충전(+), 사용(-) 입력: +40
현재 연료: 540 - 충전(+), 사용(-) 입력: 
Traceback (most recent call last):
  File "<pyshell#13>", line 3, in <module>
    if action[0] == '+':
IndexError: string index out of range
>>> 
>>> fuel = 500
... while fuel > 50:
...     action = input(f"현재 연료: {fuel} - 충전(+), 사용(-) 입력: ")
...     if action[0] == '+':
...         fuel += int(action[1:])
...         
SyntaxError: multiple statements found while compiling a single statement
