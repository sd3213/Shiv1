#palindrome for string

s=input()
rev_s=""

for i in s[::-1]:
    rev_s +=i
    # print(rev_s)

if s== s[::-1]:
    print ("yes , this is palindrome")

else:
    print("No")

# ------------------------------------------------------------------------

#Palindrome integer

# s=int(input())
# temp=s
# rev_s=0

# while(s>0):
#     digit= s%10
#     rev_s=rev_s*10 + digit
#     s=s//10

# print(rev_s)

# if(temp==rev_s):
#     print("this is a palindrome number")

# else:
#     print("this is not a palindrome number")

