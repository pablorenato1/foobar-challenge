def search(l):
    i = 1
    layerFinal = []
    for e in l:
        clist = l[:]
        clist.pop(-i)
        soma = sum(clist)
        if soma > 0 and (soma%3) == 0:
            layerFinal.append(clist)
        if len(clist) > 1:
            temp = search(clist)
            if temp:
                for t in temp: 
                    if not t in layerFinal: layerFinal.append(t)
        i +=1
    return layerFinal

def solution(l):
    l.sort(reverse=True)
    soma = sum(l)
    if soma!= 0 and (soma%3) == 0:
        return "".join(str(e) for e in l)
    t = search(l)
    if not t:
        return 0
    t = sorted(t,key= lambda i: len(i), reverse=True)
    return "".join(str(e) for e in t[0])

print(solution([1,1,2]))