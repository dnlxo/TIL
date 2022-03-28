def partial(s) :
    partials = []
    partials.append(s)
    for j in range(1, len(s)) :
        for i in range(len(s)-j+1) :
            partials.append(s[i:i+j])
    return partials

print(partial('pencil'))
