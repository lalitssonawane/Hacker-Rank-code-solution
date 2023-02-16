def minimumBribes(q):
    count = 0
    d = dict(enumerate(q,1))
    for i in range(len(d),1,-1):
        if d[i]==i:
            continue
        if d[i-1]==i:
            d[i-1] = d[i]
            count+=1
        elif d[i-2]==i:
            d[i-2],d[i-1] = d[i-1],d[i]
            count+=2
        else:
            return "Too chaotic"
    return count

for _ in range(int(input())):
    n = int(input())
    q = list(map(int, input().split()))
    print(minimumBribes(q))