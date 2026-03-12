a=int(input("k :"))
b=[]
c=0
for i in range(1,a//2+1):
    if a%i==0:
        b.append(i)
        c+=i
print(b)
if c==a:
    print("Perfect number ")
else:
    print("Not a perfect number")
        
