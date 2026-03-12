a,b,c=0,1,0
n=int(input("enter number : "))
print(a,b,sep="\t",end="\t")
while a+b<=n:
    c=a+b
    print(c,end="\t")
    a=b
    b=c
input()
