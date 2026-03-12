n=input("n: ")
l=len(n)
s=[]
a=sorted(n)
for i in range(0,l):
    if a[i]!="`":
             print(a[i],a.count(a[i]))
             s.append(a[i])
    for j in range(1,l):
         if a[i]==a[j]:
             a[j]="`"
    
print(s)
