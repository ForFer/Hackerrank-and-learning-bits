n = int(input())

names = {}
for _ in range(n):
    data = list(map(str,input().split()))
    names[data[0]] = data[1]

queries = []
while True:
    try:
        q = input()
        if q in names.keys():
            s = q + '=' + names[q]
            queries.append(s)
        else:
            queries.append("Not found")
    except EOFError:
        break
        
for q in queries:
    print(q)
