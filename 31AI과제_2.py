Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def is_prime(n):
...     def is_prime(n):
...         return False
...     if n == 2:
...         return True
...     if n % 2 == 0:
...         return False
...     for i in range(3, int(n ** 0.5) + 1, 2):
...         if n % i == 0:
...             return False
...         return True
...     n = int(input("양의 정수를 입력하세요: "))
...     print("소수입니다." if is_prime(n) else "소수가 아닙니다.")
... 
...     
>>> 
>>> 
>>> print("소수입니다." if is_prime(n) else "소수가 아닙니다.")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print("소수입니다." if is_prime(n) else "소수가 아닙니다.")
NameError: name 'n' is not defined
>>>  n = int(input("양의 정수를 입력하세요: "))
...  
SyntaxError: unexpected indent
>>> n = int(input("양의 정수를 입력하세요: "))
양의 정수를 입력하세요: 43
>>> 
>>> print("소수입니다." if is_prime(n) else "소수가 아닙니다.")
소수입니다.
