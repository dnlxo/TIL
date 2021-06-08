def solution(gems):
    num_of_kinds = len(set(gems))
    M = len(gems)
    a, b = 0, 0
    gems.append(None)
    ans = []
    dic = {gems[0] : 1}
    while a < M or b < M : 
        if len(dic) == num_of_kinds : 
            ans.append([a+1,b+1])
            if dic[gems[a]] == 1 : 
                del dic[gems[a]]
            else : 
                dic[gems[a]] -= 1
            a += 1
            
        elif len(dic) < num_of_kinds : 
            b += 1
            if b == M : 
                break
            if gems[b] in dic : 
                dic[gems[b]] += 1
            else : 
                dic[gems[b]] = 1
            
    return sorted(ans, key = lambda x: x[1] - x[0])[0]
