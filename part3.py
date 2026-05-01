# a=1
# while a<=30:
#     print(a)
#     a+=1


# a=1234
# s=1
# while a!=0:
#     s=a%10
#     print(s)
#     a//=10

# a=123
# c=a
# s=0
# while a!=0:
#     s=a%10+s*10
#     # print(s)
#     a//=10
# print(s)
# if c==s:
#     print("palindrome")
# else:
#     print("not")

# import random
# num=random.randint(1,10)
# print(num)
# a=int(input("guess no:="))
# if a==num:
#     print("you right")
# else:
#     print("not right")

# import random
# num=random.randint(1,10)
# tries=0
# while True:
#     guess=int(input("guess no:="))
#     if num==guess:
#         tries+=1
#         print(f" you are right guess in {tries}time")
#         break
#     elif num<guess:
#         tries+=1
#         print("go lower")
#     else:
#         tries+=1
#         print("go higher")


# is_game_on = True  # Pehle variable ko True rakha

# while is_game_on:
#     guess = int(input("guess no:="))
#     if num == guess:
#         print("Sahi guess!")
#         is_game_on = False  # Isse loop agli bar nahi chalega
#     else:
#         print("Phir se try karo")

# def sum( a, b):
#     print(f"hello sum is {a//b}")
# sum(3,9)
# sum(b=3,a=9)# //keyword argument

# def sum( a, b=2):
#     print(f"hello sum is {a//b}")
# sum(10,5) #positionla argument replace mar denga 


# def palindrome(st):
#     rev=""
#     for i in range(len(st)-1,-1,-1):
#         rev=rev+st[i]
#     if rev==st:
#         print(f"{st} is palindroma")
#     else:
#         print(f"{st} is not palindroma")

# palindrome("akash")
# palindrome("naman")

# def hello():
#     return print("hello are you")
# hello()


# import random
# target=random.randint(1,100)
# tries=0
# while True:
#     a=int(input("guess number"))
#     if(a==target):
#         tries+=1
#         print(f"you get it in {tries} chance")
#     elif(a>target):
#         tries+=1
#         print("go lower")
#     else:
#         tries+=1
#         print("go higher")






# def hh(name="yadav"):
#     print(f"heelo {name}")


# hh();
# hh("ak")
# jo fn call ke timew bhejnge wahi jayenga boss kyoki defaukt value
# replace ho jayenga boss



