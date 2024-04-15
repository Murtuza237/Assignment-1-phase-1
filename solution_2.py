m=int(input())
n=input()
a=[]
a[1:]=n
for ele in a:
    if ele=="," or ele==" ":
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
d.sort()                             
c=int(input())   
for i in d:
    if i==c:
        print(len(d)-1-d[::-1].index(c))
        break
else:
    print("Better Luck Next Time")
