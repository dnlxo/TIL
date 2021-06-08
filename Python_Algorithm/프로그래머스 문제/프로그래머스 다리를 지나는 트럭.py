from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_going = deque([])
    truck_weights = deque(truck_weights)
    now_weight = 0
    cnt = 0

    while True :

        cnt += 1
        for truck_on_bridge in truck_going : 
            truck_on_bridge[1] += 1

        if truck_going :
            if truck_going[0][1] > bridge_length :
                now_weight -= truck_going[0][0]
                truck_going.popleft()



        if truck_weights :
            if now_weight + truck_weights[0]  <= weight : 
                next_truck = truck_weights.popleft()
                truck_going.append([next_truck, 1])
                now_weight += next_truck

        if not truck_going :
            break
            
    answer = cnt
    return answer
