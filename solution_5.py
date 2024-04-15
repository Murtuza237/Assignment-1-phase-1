def arrange(n=[]):
    for ele in n:
         if ele==" ":
             n.remove(ele)       
    a=[]
    for i in n:
        if i=='1':
            a.append(i)
        elif i=='2':
            continue    
    for i in n:
        if i=='2':
            a.append(i)
        elif i=='1':
            continue 
    return a
z=int(input())
r=[]
for i in range(z):
    y=int(input())
    x=input()
    ilist=list(x)
    r.append(arrange(ilist))
e=""
for ele in r:
   for i in ele:
       e=e+i+" "
   print(e[:-1])
   e=""
