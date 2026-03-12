#if the number digit's in a number  are powered by it's length and added is equal to its value then it is a Armstrong Ex:- 153
n=input("n: ")
l=len(n)
sum=0
for i in n:
    sum+=pow(int(i),l)
print(f"sum of powers : {sum}")
if sum==int(n):
    print(f"{n} is a Armstrong number")
else:
    print(f"{n} is not a Armstrong number")
input()
