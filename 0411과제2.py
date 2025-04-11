
#7-21
def 회문(s):
    s = s.lower()              
    s = s.replace(" ", "")     
    s = s.replace(".", "")      
    return s == s[::-1]        

단어_혹은_문장 = input("입력하셈: ")

if 회문(단어_혹은_문장):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

#7-25
eng_kor_dict = {}

while True:
    command = input("$ ")

    if command == 'q':
        break

    if command.startswith('<'):
        
        try:
            eng, kor = command[1:].split(":")
            eng_kor_dict[eng.strip()] = kor.strip()
        except ValueError:
            print("입력 형식은 <영어단어:한글단어 입니다.")

    elif command.startswith('>'):
        
        word = command[1:].strip()
        if word in eng_kor_dict:
            print(f"{word}: {eng_kor_dict[word]}")
        else:
            print("해당 단어가 사전에 없습니다.")

    else:
        print("명령 형식이 올바르지 않습니다.")

