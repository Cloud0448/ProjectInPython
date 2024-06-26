'''
숫자 맞추기 게임
1부터 100까지 무작위 숫자를 생성,
숫자를 입력하면 무작위 숫자와 비교해서 숫자가 큰지 작은지를 알려준다. 
숫자를 맞추면 몇 회 안에 맞췄는지 알려주고 게임을 종료한다. 
'''

import random

# 1 부터 100까지 무작위 숫자 생성
number = random.randint(1, 100)

# 몇 회 시도했는지 저장하는 변수
num_of_guesses = 0

while True:
    # 숫자 입력받기
    guess=int(input("1부터 100까지의 숫자를 입력하세요: "))
    
    num_of_guesses += 1
    
    # 조건문 if 사용
    # 사용자가 입력한 숫자랑 랜덤함수가 생성한 숫자 비교
    # 추측한 숫자가 더 크다면 "입력한 숫자가 너무 큽니다." 라고 출력
    if guess > number :
        print('DOWN')
    #  더 작다면 "입력한 숫자가 너무 작습니다." 라고 출력
    elif guess < number :
        print('UP')
    # 같다면 "축하합니다. {0}회만에 숫자를 맞췄습니다. 라고 출력"
    else : 
        print('Congratulations! Correct answer in %d times!' % (num_of_guesses))
        break
    