T = int(input())

def cal_3(d_index, mine_index):

    if i == 0:
        D[d_index][0] = gold_map[mine_index]
        D[d_index][1] = gold_map[mine_index]
        D[d_index][2] = gold_map[mine_index]
    else:
        try:
            D[d_index][0] = D[d_index - 1][0] + gold_map[mine_index]
        except:
            D[d_index][0] = gold_map[mine_index]

        try:
            D[d_index][1] = D[d_index][1] + gold_map[mine_index] 
        except:
            D[d_index][1] = gold_map[mine_index]

        try:
            D[d_index][2] = D[d_index + 1][2] + gold_map[mine_index]
        except:
            D[d_index][2] = gold_map[mine_index]


result = []  # T개의 결과 저장.

for _ in range(T):

    n, m = map(int, input().split())

    gold_map = list(map(int, input().split()))

    D = [[0, 0, 0] for _ in range(n)]
    print(D)

    for i in range(m):
        for j in range(n):
            cal_3(j, j + j * m)

    print("D: ", D)
        
    
for _ in result:
    print(_)    
