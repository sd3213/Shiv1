num=int(input("enter the number \n"))

factorial=1


if(num<0):
    print("this is not possible")

elif(num==0):
    print("1")

else:

    for i in range (1,num+1):
        factorial = factorial*i
        print(i)

    print(factorial)
