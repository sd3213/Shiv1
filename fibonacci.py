#0, 1,1,2,3,5,8,11

a=0
b=1
n=int(input())
if n==1:
    print(a)

else:

    while(n>0):
        print(a ,end=" ")
        x=a+b
        a=b
        b=x
        n-=1


