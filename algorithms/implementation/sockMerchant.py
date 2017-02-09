n = int(input())
socks = list(map(int, input().split())) 

pairs = 0
while(socks):
    s = socks.pop(0)
    if(s in socks):
        socks.pop(socks.index(s))
        pairs+=1
    
print(pairs)
