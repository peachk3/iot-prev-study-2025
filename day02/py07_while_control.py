# while문
# for문과 동일

loop = 10
while loop >= 0 : # loop 변수값이 0보다 큰 동안 계속
    print(loop, end='\t')
    loop = loop - 1

print()


# 위의 while문과 동일한 결과 출력
for i in range(10, -1, -1):
    print(i)

print()

# 무한반복
num = 0
while True :
    print('Hello', num)
    num = num + 1