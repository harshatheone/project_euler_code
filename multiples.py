s = 999
p=[]
q=[]
for i in range(1, s+1):
    if i % 3 == 0:
        p.append(i)
    if i % 5 ==0:
        q.append(i)

m = set(p + q)
print(p)
print(q)
print(m)
print (sum(m))

    
