# https://www.acmicpc.net/problem/5525   IOIOI

#  코드 출처 https://donghak-dev.tistory.com/27
import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
S = input().rstrip()

answer = 0
count = 0
i = 1

while i < M - 1:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        count += 1
        if count == N:
            count -= 1
            answer += 1
        i += 1
    else:
        count = 0
    i += 1

print(answer)


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

"""

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
        else:
            pass

print(count)
"""