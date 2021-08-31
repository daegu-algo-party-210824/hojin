def solution(food_times, k):
    answer = 0
    
    if sum(food_times) <= k:  # 방송오류 전에 다 먹으면 -1 return.
        answer = -1
    
    
    while k >= 0:
        if answer == -1:  # 더 먹을 음식 없을때 반복문 실행필요없음.
            break
            
            
        for i in range(len(food_times)):
            
            answer = i + 1  # 먹을 음식의 인덱스
            
            if food_times[i] == 0:  # 다 먹은 음식 패스.
                pass
            else:                    
                food_times[i] -= 1  # 음식을 먹음. 남은음식 먹는데 걸리는 시간 1 차감.
                k -= 1  # 먹는동안 흐른 시간 -1 차감
                print("index=", answer, "after: ",food_times)
                

    return answer