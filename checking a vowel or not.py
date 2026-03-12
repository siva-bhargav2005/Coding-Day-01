print("enter 9 to quit ")
while True:
    n=input("enter :")
    if n=="9":
        break
    if n=="A" or n=="a" or n=="E" or n=="e" or n=="I" or n=="i" or n=="O" or n=="o" or n=="U" or n=="u":
        print(f"{n} is a Prime number")
    else:
        print(f"{n} is not a Prime number")   
input()
