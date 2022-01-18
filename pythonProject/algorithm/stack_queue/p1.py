# s "[]()"
from algorithm.stack_queue.structures import Queue


def is_valid(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    opener = "{[("
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False
    return not stack

def get_card(num):
    queue = Queue([1, 2, 3, 4])
    while len(queue) > 1:
        # 1. 제일 위 카드를 버린다.
        front = queue.pop()
        # 2. 그 다음 제일 위 카드를 맨뒤로 옮긴다.
        queue.push(queue.pop())
    # 3. 한 장 남은 카드를 반환한다.
    return queue.pop()

assert is_valid("{}()")
assert is_valid("{[]}")
assert is_valid("({[]})")

assert not is_valid("{}]")

assert get_card(6) == 4
