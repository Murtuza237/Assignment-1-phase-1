m=int(input())
n=(input())
a=[]
a[1:]=n
for ele in a:
    if ele==";":
        a.remove(ele)
b=""
d=[]
for i in n:
    if (i =="-" and not b) or ('0'<=i<='9'):
        b+=i 
    elif b:
        d.append(int(b))
        b=""
if b:
     d.append(int(b))     
sum=0
for i in range(len(d)):
    sum+=d[i]
print(sum)
