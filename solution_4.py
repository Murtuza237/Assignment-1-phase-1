def turnaround(n=[]):
    c=len(n)
    d=n[1]-n[0]
    b=n[c-1]+d
    n.append(b)
    a=(len(n)//2)
    e=a//2
    for i in range(a-1,len(n)):
        print(n[i])
    for i in range(e,a-1):
        print(n[i])
    for i in range(0,e):
        print(n[i])    
        
y=[]
x=int(input())
for i in range(x-1):
    z=int(input())
    y.append(z)               
