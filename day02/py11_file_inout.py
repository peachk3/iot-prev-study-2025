# 파일 입출력

# a(추가), r(읽기), w(쓰기)
f = open('./day02/testfile.txt', mode='w', encoding='utf-8') #./day02 파일 안에 testfile 생성
# w - 모두 지우고 새로 씀 / a - 뒤에 계속 추가로 작성
# 아무것도 안함
f.write('저는 한국사람입니다.\n')
f.write('잠이 와여.\n')
f.close() # => testfile.txt 생성

print('텍스트파일이 생성되었습니다')

## 읽기
f = open('./day02/testfile.txt', mode='r', encoding='utf-8')

while True : # 무한반복
    line = f.readline() # 한줄씩 읽고
    if not line: break # 읽을 줄이 없으면 반복문 탈출

    print(line)

f.close()