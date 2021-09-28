n = int(input())

explorer = list(map(int, input().split()))

explorer.sort()

data = set(explorer)  # 구성하는 원소 구하기

print("data = ",data)

group = 0

# 공포도가 작은 순으로 그룹을 만들고, 공포도가 큰 사람은 마을에 남겨두기.
# for i in data:
#     group += explorer.count(i) // i  
# 1 4 1 5 2 = 3 인데 2가 출력.


while True:

    if len(explorer) == 0:
        break
    else:
        head = explorer[0]

    if len(explorer) < head:
        break
    else:
        for i in range(head):
            explorer.pop(0)
        group += 1
        
    print("left: ", explorer)

print(group)

# 완성
