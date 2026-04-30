# a=10
# b=17
# print(a+b,b-a,a*b,b/a)
# print(int(b/a))
# print(b//a)
# print(2**3)





# a=12
# b=13
# print(a!=b)
# print(23>23)
# print("abc">"acd")


# print(not 12==12) result ka ulta print kr denga
# print(True and bool(0))
# dhyan rakhna used yahi honge boss


# a=13
# if a>15:
#   print("i")
# else:
#   print("jk")  


# money=int(input("give money:"))
# if money==10:
#     print("i")
# elif money==100:
#   print("jk") 
# else:
#   print("jkk")   


# num1=int(input("first"))
# num2=int(input("second"))
# if num1>num2:
#   print("a great")
# elif num1==num2:
#   print("a==b")
# else:
#   print("num2 great")


# gend=(input("batao:"))
# if gend=="male":
#     print("l")
# else:
#   print("b")

# n=int(input("number="))
# if n%2==0:
#     print("even")

# else:
#     print("odd")


# year=int(input("century year:"))
# if year%100==0:
#     print("sachin")
# else:
#     print("bobby")




# for i in range(101):
#   # 0:101:1;
#   print(i)

# let print table of 6
# for i in range(6,(6*10)+1,6):
#     print(i)

# a="thjhwjh jshfhf sfhjhfk sdjhfnjshh"
# print(len(a))

# for i in range(len(a)):
# for i in range(33):
#     print(a[i])



# for i in range(1,21):
#     if i==16:
#         print("break ststemeint executed")
#         break
#     print(i)
# else:
#     print("break executed not")
#     Jab else loop ke saath juda hota hai (indentation for ke barabar), toh Python use tabhi chalata hai jab loop poora khatam ho jaye. Agar loop ke beech mein break aa gaya, toh Python else ko skip kar deta hai.


# n=int(input("enetr number="))
# for i in range(1,11):
#       print(f"{n}*{i}={n*i}")


# sum=0
# for i in range (1,101):
#     sum+=i
# print(f"your sum is={sum}")


# fact=1
# n=int(input("enetr number="))
# for i in range (1,n+1):
#     fact*=i
# print(f"your fact is={fact}")


# even=0
# odd=0
# n=int(input("enetr number="))
# for i in range (1,n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"your sum is={even} and {odd}")


# sum=0
# n=int(input("enetr number="))
# for i in range (1,n):
#     if n%i==0:
#         sum+=i

# if sum==n:
#     print(f"{n} i perfect")



# su=0
# n=int(input("enetr number="))
# for i in range (1,n+1):
#     if n%i==0:
#         su+=1
# print(f"total factor is {su}")




# a="naman"
# b=" yadav"
# c=""
# print(a+b)
# for i in range (len(a)-1,-1,-1):
#     c=c+a[i]
# print(c)

# if c==a:
#     print("palindrome")


# prime number code
# a=int(input("enter"))
# if a>2:
#  for i in range(2,a):
#     if a % i == 0:
#         print("Not prime")
#         break
#  else:
#     print("Prime")  
# else:
#       print("Primee")    


# n=1
# a=int(input("enter"))
# for i in range(1,a+1,1):
#     if i%2==0:
#         n*=i
# print(f"product is {n}")        



# check armstrong number ka code likh
# a=int(input("enter"))
# l=0
# temp=a
# while temp!=0:
#     l+=1
#     temp//=10
# temp=a
# ans=0
# while temp!=0:
#     ans+=((temp%10)**l)
#     temp//=10

# if ans==a:
#     print("armstrong")
# else:
#     print("not aramstrong")


# a="markram"
# w=a
# in python string immutable

# k=len(a)
# print(a)
# a = list(a)
# for i in range(0,k//2):
#     c=a[i]
#     a[i]=a[len(a)-i-1]
#     a[len(a)-i-1]=c
# p = "".join(a)   
# print(p)
# if(p==w):
#     print("palindrome")
# else:
#     print("not palindrome")


# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end ="")
#     print()  


# a="naman"
# v=0
# a = a.lower()
# a=list(a)
# for i in range (0,len(a)):
#     if(a[i] in "aeiou"):
#         v+=1 
# print(f"vowel ={v} and cpns={len(a)-v}")



# n=int(input("number enter kr re"))
# a=0
# for i in range (1,n):
#     if n%i==0:
#         a+=i
# if(a==n):
#     print("perfect")
# else:
#     print("not perfect")

#a = int(input("enter number: "))

#temp = a
# sum_digits = 0
# rev = 0

#while temp != 0:
#     digit = temp % 10
#     sum_digits += digit
#     rev = rev * 10 + digit
#     temp //= 10

#print(f"sum = {sum_digits}")
#print(f"reverse = {rev}")

#if rev == a:
#     print("palindrome")
#else:
#     print("not palindrome")  

# n = int(input("enter terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c 


