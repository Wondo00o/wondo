Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("섭씨(C) 화씨(F)")
섭씨(C) 화씨(F)
>>> print("-"*15)
---------------
>>> for celsius in range(0,51,10):
...     fahrenheit=(9/5)*celsius+32
...     print(f"{celsius:<7}{farenheit:<7.1f}")
... 
...     
Traceback (most recent call last):
  File "<pyshell#6>", line 3, in <module>
    print(f"{celsius:<7}{farenheit:<7.1f}")
NameError: name 'farenheit' is not defined. Did you mean: 'fahrenheit'?
>>> [DEBUG ON]
>>> [DEBUG OFF]
>>> print("섭씨(C) 화씨(F)")
섭씨(C) 화씨(F)
>>> print("-"*15)
---------------
>>> for celsius in range(0,51,10):
...     fahrenheit=(9/5)*celsius+32
...     print(f"{celsius:<7}{fahrenheit:<7.1f}")
... 
...     
0      32.0   
10     50.0   
20     68.0   
30     86.0   
40     104.0  
50     122.0  
>>> celsius = float(input("섭씨 온도를 입력하세요: "))
섭씨 온도를 입력하세요: 33
>>> fahrenheit = (9/5) * celsius + 32
>>> print(f"섭씨 {celsius}°C는 화씨 {fahrenheit:.1f}°F 입니다.")
섭씨 33.0°C는 화씨 91.4°F 입니다.
