import itertools

def solution(orders, course):
    orders_ = []
    for i in orders : 
        k = ''.join(sorted(i))
        orders_.append(k)
    menu = {}
    for i in course :
        for j in orders_ : 
            for k in itertools.combinations(j, i) :
                if ''.join(list(k)) in menu : 
                    menu[''.join(list(k))] += 1
                else : 
                    menu[''.join(list(k))] = 1
    menu_ = []
    max_cnt = []
    for i in menu :
	    menu_.append((i,menu[i]))
    menu_ = sorted(menu_, key = lambda x : x[1], reverse = True)
    for i in course :
        for j in menu_ :
            if len(j[0]) == i :
                max_cnt.append(j[1])
                break
    answer = []
    for i in range(len(course)) : 
        for j in menu_ : 
            if len(j[0]) == course[i] :
                if j[1] == 1 : 
                    break
                if j[1] == max_cnt[i] : 
                    answer.append(j[0])
    answer.sort()
    return answer
