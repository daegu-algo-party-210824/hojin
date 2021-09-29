# 듣보잡

a, b = map(int, input().split())

list_1 = []  # 듣도 못한 사람 
list_2 = []  # 보도 못한 사람

for i in range(0,a):
    name = input()
    list_1.append(name)

for i in range(0, b):
    name = input()
    list_2.append(name)

list_1 = set(list_1)
list_2 = set(list_2)

db_names = list_1 & list_2

print(len(db_names))
for name in sorted(db_names):
    print(name)
