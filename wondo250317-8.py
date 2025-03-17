Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> a = float(input("밑변을 입력하세요: "))
밑변을 입력하세요: 2
>>> b = float(input("높이를 입력하세요: "))
높이를 입력하세요: 3
>>> c = math.sqrt(a**2 + b**2)
>>> print(f"빗변의 길이는 {c:.2f} 입니다.")
빗변의 길이는 3.61 입니다.
>>> for i in range(1, 11):
...     print(f"2^{i} = {1 << i}")
... 
...     
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64
2^7 = 128
2^8 = 256
2^9 = 512
2^10 = 1024
>>> n = int(input("숫자를 입력하세요: "))
숫자를 입력하세요: 35
>>> print(n % 2 == 0)
False
