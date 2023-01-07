n=int(input("enter . no. of terms:"))
f=1
s=0
for i in range (1,n+1):
    f=f*(i+1)
    s=s+(i/f)
    print("sum:",s)
