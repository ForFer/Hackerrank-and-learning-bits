s=input()
i = int(s)
s = []
while(int(i)>0):
    s.append(input())
    i=i-1

s1=input()
i = int(s1)
j = i
s1 = []
while(int(i)>0):
    s1.append(input())
    i=i-1
res = [0 for n in range(len(s1))]
for i in range(len(s1)):
    for j in range(len(s)):
        if(s1[i]==s[j]):
            res[i]+=1
    print(res[i])
