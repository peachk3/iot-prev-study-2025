# 모듈

import py10_function as calc

calc.multi(10, 4)

# 수학 함수를 편하게 모아둔 모듈 
import math

result = math.pow(2, 10)
print(result) # 실수 출력 (1024.0)

result = math.log2(4)
print(result)

## 패키지 - 모듈들을 모아둔 디렉토리(폴더)
## pip install requests -> 터미널에서 명령어 입력해서 다운받기

import requests

res = requests.get('https://www.naver.com') # 네이버 사이트를 접속하라
print(res.status_code) # 200

print(res.content)