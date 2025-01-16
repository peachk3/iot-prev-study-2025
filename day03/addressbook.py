# 주소록 프로그램

import contact
import os # 운영체제에 사용할 가능 모듈

# 5. 연락처를 입력받는 함수
def set_address():
    try:
        name, phone, email, addr = input('정보 입력(이름, 전화번호, 메일, 주소 순) : ').split(',')
        # print(name, phone, email, addr)
        # 8. 컨택트 객체 생성, 리턴
        address = contact.Contact(name, phone, email, addr)
        return address # Contact 객체 리턴
    except ValueError:
        print('데이터를 정확히 입력하세요')
        return None # 아무것도 아닌거

# 11. 연락처 출력
def get_address(lst_contact):
    for i in lst_contact:
        print(i)

# 13. 연락처 삭제
# 17. 연락처 삭제 함수 변경. 삭제여부 리턴
def del_address(lst_contact, name):
    result = False # 아무것도 삭제되지 않았음
    for i, item in enumerate(lst_contact): # 각 객체에 번호를 매겨주는 클래스
        if item.isNameExist(name):
            del lst_contact[i] # del 메모리에서 완전삭제
            result = True # 삭제했음
    
    return result # 삭제 여부 반환

# 9. 콘솔화면 클리어 함수
def clear_console():
    command = 'clear' # Linux, unix 클리어 명령어
    if os.name in ('nt', 'dos') : # 운영체제가 윈도우라면
        command = 'cls' # Windows 클리어 명령어

    os.system(command) # 콘솔에 명령어 실행

## 15. 파일DB 저장 함수
def save_contact(lst_contact):
    f = open('./day03/address_db.txt', mode='w', encoding='utf-8')
    for item in lst_contact:
        f.write(item.getName() + '/')
        f.write(item.getPhone() + '/')
        f.write(item.getEmail() + '/')
        f.write(item.getAddr() + '\n')

    f.close() # 파일을 열었으면, 끝난 후 파일 반드시 닫아야 함!!

## 16. 파일DB 로드 함수
def load_contact(lst_contact):
    f = open('./day03/address_db.txt', mode='r', encoding='utf-8')
    while True:
        line = f.readline() # 도경/1234/naver.com/부산
        if not line: 
            break # 줄에 아무글도 없으면 빠져나감
        
        # 25.01.16. 15:53 도경. (오류 수정시 작성)
        # \n으로 오류발생 -> \n을 리스트 저장 전에 삭제해야 함 (replace)
        lines = line.replace('\n','').split('/') # lines는 4개의 문자열을 가지는 리스트가 됨
        # lines = ['도경', '1234','naver.com','부산']
        # lines[0] == '도경'
        address = contact.Contact(name=lines[0], phone=lines[1], email=lines[2], addr=lines[3]) 
        lst_contact.append(address)
    
    f.close()

# 6. 프로그램 실행 함수
def run():
    # 10. 주소 정보들을 담을 변수(리스트)
    lst_contact = [] # 빈 리스트
    load_contact(lst_contact)

    # set_address()
    clear_console() # 화면 클리어
    while True: 
        sel_menu = get_menu()
        clear_console()
        if sel_menu == 1 : # 연락처 추가
            info = set_address()

            if info is None:
                pass
            else:
                lst_contact.append(info) # 10. 주소 정보 담기
                print('추가되었습니다')
                 
            input()

        elif sel_menu == 2 : # 연락처 출력
            get_address(lst_contact)
            input()

        elif sel_menu == 3 : # 연락처 삭제
            name = input('삭제할 이름 입력: ')
            res = del_address(lst_contact, name)
            if res == True:
                print('삭제되었습니다')
            else:
                print('삭제할 데이터가 없습니다')

            input() # 단순 입력대기

        elif sel_menu == 4 : # 종료
            save_contact(lst_contact)
            break # 프로그램 종료
        else:
            pass
        
        clear_console()

# 7. 메뉴 구성
def get_menu():
    str_menu = ('주소록 프로그램 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 종료\n')
    print(str_menu)

    # 예외처리 try - except - (finally) 키워드 사용
    try:
        menu_num = int(input('메뉴입력: ')) # 숫자를 표현하는 문자열
    except Exception:
        print('예외발생!')
        menu_num = 0 # 메뉴와 관계없는 숫자
        
    return menu_num # 문자열(1~4)을 정수로 변경

#1. 프로그램 시작
if __name__ == '__main__' :
    #pass # if, for, while, 함수 등에서 오류를 없애는 방법
    # print('주소록 프로그램')
    # 3. 클래스 실행 - 객체를 생성
    # first = contact.Contact('박도경','010-7447-1896', 'doo062991@gmail.com', '부산')
    # print(first)
    run() # 제일 처음 실행되는 함수

# print('프로그램 종료')
