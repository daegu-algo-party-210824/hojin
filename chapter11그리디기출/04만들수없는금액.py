n = int(input())

coin = list(map(int, input().split()))

money = coin  # 만들 수 있는 금액 리스트

for i in range(n):
    sum = coin[i]
    for j in range(n):
        if i == j:
            pass
        else:
            sum += coin[j]
            money.append(sum)

money = set(money)

print("만들 수 있는 금액: ",money)

min_money = 1

for i in range(1, max(money)):
    if i not in money:
        min_money = i
        break
    
print(min_money)

# end

