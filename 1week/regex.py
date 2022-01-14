# 정규표현식 (regular expression, regex)
# : 문자열 형식을 확인하는 식

# 언제 쓸까??
# ex) 웹 개발(아이디 유효성 검사, a@naver.com)

import re
# search(), findall(), split(), sub()
# \w: alphabet + number
# \d: number
# \s: space character

if __name__ == "__main__":
    str = "The rain in Spain"
    x = re.search("^The", str)

    print(x)