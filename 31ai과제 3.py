Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = int(input("양의 정수를 입력하세요: "))
양의 정수를 입력하세요: 5
>>> sum_of_squares = sum(i**2 for i in range(1, n+1))
>>> print(f"1^2 + 2^2 + ... + {n}^2 = {sum_of_squares}")
1^2 + 2^2 + ... + 5^2 = 55
>>> depth = 30
>>> day_climb = 7
>>> night_slide = 5
>>> current_height = 0
>>> days = 0
>>> while True:
...     days += 1
...     current_height += day_climb
...     if current_height >= depth:
...         break
...     current_height -= night_slide
...     print(f"달팽이는 {days}일째에 우물을 탈출한다.")
... 
...     
달팽이는 1일째에 우물을 탈출한다.
달팽이는 2일째에 우물을 탈출한다.
달팽이는 3일째에 우물을 탈출한다.
달팽이는 4일째에 우물을 탈출한다.
달팽이는 5일째에 우물을 탈출한다.
달팽이는 6일째에 우물을 탈출한다.
달팽이는 7일째에 우물을 탈출한다.
달팽이는 8일째에 우물을 탈출한다.
달팽이는 9일째에 우물을 탈출한다.
달팽이는 10일째에 우물을 탈출한다.
달팽이는 11일째에 우물을 탈출한다.
달팽이는 12일째에 우물을 탈출한다.
>>> print("하...days에 1했어야하는데...")
하...days에 1했어야하는데...
>>> print("달팽이는 13일째에 탈출합니다.")
달팽이는 13일째에 탈출합니다.
