def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    # 2단계 
    ans = ''
    for i in new_id : 
        if i.isalnum() or i in '-_.' : 
            ans += i
    # 3단계 중요@@@@
    while '..' in ans : 
        ans = ans.replace('..','.')
    # 4단계
    if ans != '' :
        if ans[0] == '.' : 
            ans = ans[1:]
    if ans != '' :
        if ans[-1] == '.' : 
            ans = ans[:-1]
    # 5단계
    if ans == '' : 
        ans += 'a'
    # 6단계
    if len(ans) > 15 : 
        ans = ans[:15]
    # 7단계
    if len(ans) <= 2 : 
        while len(ans) != 3 : 
            ans += ans[-1]
    return ans
