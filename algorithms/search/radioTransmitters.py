"""
Author: Fernando Collado
Github: ForFer
Hackerrank: F0rz4
"""

"""
https://www.hackerrank.com/challenges/hackerland-radio-transmitters
"""

def search_next_index(count, x, marked, n, k, h=0):
    h_marked_index = -1
    if h+1==n and marked[x[h]]==0:
        marked[x[h]]=2
        return n, count-1

    for i in range(h, n-1):
        xi = x[i]
        temp = k
        if i+k<len(x):
            for j in range(i+k, i, -1):
                if x[j]-xi <= temp:
                    marked[x[j]] = 2
                    h_marked_index = j
                    count-=1
                    break
                else:
                    continue
        if h_marked_index != -1:
            marked[x[i]] = 1
            count-=1
            break
    return h_marked_index, count

def mark_next_index(count, x, marked, n, k, h_marked_index):
    h = h_marked_index
    l = -1    
    if h == n:
        return l, count
    xh = x[h]
    for i in range(h+1, n):
        xi = x[i]
        if xi-xh <= k:
            marked[xi] = 1
            count-=1
        else:
            l = i-1
            break
    return l, count

#n,k = input().strip().split(' ')
#n,k = [int(n),int(k)]
#x = []
#for i in input().split():
#    if int(i) not in x:
#        x.append(int(i))
#x.sort()

#marked = {i:0 for i in x}
#count = len(x)
#n = len(x)
#print(x)
#h_marked_index,count = search_next_index(count, x, marked, n, k)
#n_marked_index,count = mark_next_index(count, x, marked, n, k, h_marked_index)

#while count>0:
#    h_marked_index,count = search_next_index(count, x, marked, n, k, n_marked_index+1)
#    n_marked_index,count = mark_next_index(count, x, marked, n, k, h_marked_index)
    
#transmitters = 0

#for k in marked:
#    if marked[k] == 2:
#        transmitters+=1

#print(transmitters)

# NOT MY SOLUTION (belongs to user: humoyun_ahmad ), BUT FASTER AND MORE ACCURATE
n,k = map(int, input().split())
arr = [int(x) for x in input().split()]
arr.sort()
l=len(arr)
count=0
last=arr[0]
i=0
while l>i:
    count+=1
    while l>i and arr[i]-k<=last:
        i+=1
    last=arr[i-1]
    while l>i and arr[i]-k<=last:
        i+=1
    if l>i:
        last=arr[i]

print (count)
