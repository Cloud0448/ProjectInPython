import requests

def currency_converter(amount, from_currency, to_currency):
    #API 호출 url
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data=response.json
    
    #환율 계산 
    exchange_rate = data['rates'][to_currency]
    # 1.결과 환율을 소수점 2자리 까지 표시 하세요
    
    # 2. result 리턴


print("환율 변환기")
print("==========================")

while True:
    try:
        # 3. 변환하려는 금액 입력 받기 
        amount = 0
         
        from_currency = input("어떤 화폐에서 변환하시곘습니까? (예: USD, KRW): ").upper()
        to_currency =input("어떤 화폐로 변환하시곘습니까? (예: USD, KRW): ").upper()

        # 4. 환율 계산하는 함수 호출
        
        # 5. 결과 출력. from current는 to currency 입니다~
        
        # 계속 변환할지 묻기
        choice = input("계속 변환하시겠습니까? (Y/N):").upper()
        if choice != "Y":
            break;
        
        # 6. N을 선택할 경우 프로그램을 종료한다는 메시지 출력
        # 7. 다른개발자들이 환율코드를 확인할 수 있도록 맨위에 주석으로 화폐목록을 적어주세요 ex) 미국(USD)..
    except:
        print("올바른 값을 입력하세요.")