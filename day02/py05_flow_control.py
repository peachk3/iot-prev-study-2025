# 흐름제어
# if, for, while

## int(정수화), flaot(실수화), double(복소수화)
age = int(input('나이를 입력하세요 > ')) # age에 문자열이 입력 30 -> '30'

## if문을 시작하겠다는 의미하는 마지막 단어 -> :
if age > 19 and age < 61 :
    # if문이 참(True)이면 아래의 구문을 실행
    # if문(흐름제어) 안으로 들어왔다!
    print('술 살 수 있음')
elif age > 60 : # 다른 조건이 필요할 때 (else if) - 여러 번 사용 가능
    print('술 그만 마시세여')
else:
    # if문이 거짓(False)이면, 아래 구문을 실행
    print('안돼')
