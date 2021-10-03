# https://www.acmicpc.net/problem/5525

import sys

n = int(sys.stdin.readline())  # O의 갯수 Pn

m = int(sys.stdin.readline())  # 문자열 길이

s = sys.stdin.readline()  # 문자열

pn = "".join("IO" for i in range(n)) + "I"  # Pn 문자열 생성


def validation(index):
    if s[index:index + n * 2 + 1] == pn:  # 인덱스부터 시작한 문자열이 Pn과 일치하면.
        return True
    else:
        return False

def find_start_i(s):
    for i in range(len(s)):
        if s[i] == "I":
            return i

start_index = find_start_i(s)

count = 0

for i in range(start_index, m - (n * 2)):
    if s[i+1] == "I":  # 연속해서 I면 pass
        continue
    else:
        if validation(i) is True:
            count += 1
            i += 2
        else:
            pass

print(count)

"""
1
13
OOIOIOIOIIOII

출력 4

2
13
OOIOIOIOIIOII

출력 2
"""