n=input("str: ")
if len(n)==1 :
    print(n)
else:
    print(n[-1]+n[1:-1:]+n[0])
input()
