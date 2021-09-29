# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
 
pkmn = [] # 포켓몬 이름을 저장할 list
pkmn_dic = {} # 포켓몬 이름에 따른 번호를 저장할 dictionary
 
for i in range(n) :    
    pk = input().rstrip()
    pkmn.append(pk)
    pkmn_dic[pk] = i + 1
 
for _ in range(m):
 
    query = input().rstrip()
 
    # query가 숫자이면 list에서 조회 후 출력
    if query.isdigit() :
        print(pkmn[int(query)-1])
    # query가 문자열이면 dictionary에서 조회 후 출력
    else :
        print(pkmn_dic[query])


# 나의 틀린 코드(시간초과)

# import sys

# a, b = map(int, sys.stdin.readline().split())

# zip = []

# for i in range(0, a):
#     monster = sys.stdin.readline().rstrip()
#     zip.append(monster)

# question = []
# for i in range(0, b):
#     q = sys.stdin.readline().rstrip()
#     question.append(q)

# print(zip)
# for i in range(0, b):
#     try:  # 값이 숫자일 때 
#         if int(question[i]) + 0 >= 0:
#             print(zip[int(question[i])-1], end="\n")
#     except:  # 문자열이면
#         print(zip.index(question[i])+1, end="\n")