# 구구단 프로그램
# 2 X 1 = 2 ~ 9 X 9 = 81

for i in range(2, 10) :
    # print(i)
    for j in range(1, 10) :
        if j == 9:
            break

        # print(j)
        # print(i * j) - 값만 출력
        print(i, 'X', j, '=', i * j, end='\t')
    
    print()

