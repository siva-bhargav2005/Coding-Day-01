#Palilndrome number
n=input("n :")
temp=n[::-1]
if n==temp:
    print(f"{n} is a Palindrome")
else:
    print(f"{n} is not a Palindrome")
input()
