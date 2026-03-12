n=input("str: ")
if len(n)%2==0:
    print(n[0:len(n)//2])
elif len(n)==0:
    print("null")
else:
    print(n[len(n)//2+1:])
input()
