n=int(input("enter the number :"))
if n==1:
    print(" 1 is a perfect square")
else:
    for i in range(1,n):
        if i*i==n:
            print(f"{n} is a perfect number")
            break
    else:
        print(f"{n} is not a perfect number")
