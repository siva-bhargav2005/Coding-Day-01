n=input("str : ")
fir=""
sec=""
if len(n)==0:
    print("null")
elif len(n)==1:
    fir=n
else:
    fir=n[0::2]
    sec=n[1::2]
print(f"first: {fir}")
print(f"second: {sec}")
print(f"original: {n}")
input()
