fuel = 500 

while fuel > 50:
    action = input(f"현재 연료: {fuel} - 충전(+), 사용(-) 입력: ")
    
   
    if action[0] == '+':
        fuel += int(action[1:])
    elif action[0] == '-':
        fuel -= int(action[1:])
    
  
    if fuel <= 50:
        print("경고: 연료가 50 이하로 떨어졌습니다. 연료를 채워주세요.")
        break
