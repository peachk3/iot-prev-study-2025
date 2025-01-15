# for 문 - 프로그래밍의 꽃

# range(9) => 0,1,2,3,4,5,6,7,8
# print(range(n))

for i in range(9) : # for문 흐름제어로 들어간다 (0부터 n번째까지 출력)
    print(i, end='\n') # \n 한 줄 내림 end 인자로 출력 끝을 조정

# => i = 0 print(i), i = 1 print(i), i = 2 print(i), i = 3 print(i) ... i = 8 print(i) 과 동일함

# 1부터 10까지의 합 - 55
sum = 0
for i in range(1, 11) : # 1 ~ 10까지 
    sum = sum + i

print(sum)

sum = 0
for i in range(1, 10, 2) : # 1 ~ 9까지 2씩 증가
    print(i)

