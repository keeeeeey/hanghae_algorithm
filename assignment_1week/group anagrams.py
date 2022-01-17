# 입력 = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
import collections
from typing import List


def group_anagrams(strs: List[str]):
    word_dict = {}
    for word in strs:
        sorted_str = ''.join(sorted(word))
        if sorted_str not in word_dict:
            word_dict[sorted_str] = [word]
        else:
            word_dict[sorted_str].append(word)

    ans = [anagram for anagram in word_dict.values()]
    return ans


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))