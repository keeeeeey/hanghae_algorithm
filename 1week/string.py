if __name__ == "__main__":
    s = "hello" #s: str -> type hint
    print(s[1]) # indexing e
    print(s[-1]) # indexing reverse order o
    print(s[-2]) # l
    print(s[1:]) # slicing (***) (substring()) ello
    print(s[1:len(s)]) # ello
    # slicing
    # [start:end] (end 미포함)
    # start <=        < end
    # start: 0 생략
    # end: len(s) 생략
    print(len(s)) # 5

    # in 연산자 (문자열 안에 문자열 포함되는지?)
    print("s" in s) # False - hello 안에 s가 포함 안되있어서 False!!

    idx = s.index('e') # return index
    print(idx) # 1 - 'e'가 1번쨰 인덱스에 있다

    # join: list -> str -> list 안의 문자열을 하나의 문자열(str)로 합친다
    li = ['1', '2', '3', '4']
    s1 = "".join(li) # 사이사이에 ""안의 문자열이 들어감
    print(s1) # 1234
    s2 = s.join(li)
    print(s2) # 1hello2hello3hello4

    s = "hhhh"
    cnt = s.count('h')
    print(cnt) # s 문자열 안에 'h'가 몇개 들어가 있는지? = 4

    # 파이썬에서 배열 (정적) -> 리스트 (동적) (배여려 사이즈 변할 수 있음)
