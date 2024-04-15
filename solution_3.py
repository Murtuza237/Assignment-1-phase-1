def reflection(n):
    a=[]
    b=""
    for i in n:
        if i !=",":
            b+=i  
        else:
            a.append(b)
            b="" 
    if b:
        a.append(b)                 
    c=a[::-1]
    for b in c:
         print(b)
m=input()
n=input()
reflection(n)
