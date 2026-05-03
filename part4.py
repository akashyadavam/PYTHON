# a=12,13,14,15
# print(a[:3:])
# for i in range(len(a)):
#     print(a[i])

# help(list)
# l= [1,2,3,4,5-2,-2,-3,-4]
# print("positive number")
# for i  in range(len(l)): #yaha 0,length,1 indexx ke jaise chalta hai loop
#     if l[i]>0:
#         print(l[i],end=" ")
# print("\nnegative number")
# for i  in range(len(l)):
#     if l[i]<0:
#         print(l[i],end=" ")       
# sum=0 
# l= [1,2,3,4,5]
# for i in l:    # yaha list ke direct element uthate hain
#     sum=sum+i
# print(sum/len(l))   


# max=-1

# l=[12,13,34,25,5,242,242453,339440]
# maxx=l[0]
# for i in l:
#   if  i>max:
#     max=i
    # if i<maxx:
    #     maxx=i
# print(max)
# print(maxx)


# l=[12,13,34,25,5,242,242453,339440]
# largest=l[0]
# seclargest=l[0]
# for i in l:
#     if i>largest:
#         seclargest=largest
#         largest=i
#     elif i>seclargest:
#         seclargest=i
# print(largest,seclargest)

# l=l=[12,13,35,5,24,242,242453,339440]
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         print(f"no sorted ")
#         break
# print(l)


# tuple
# a=(1,2,3)
# print(type(a))
# print(a[0])
# for i in a:
#     print(i)

# set
# a={1,2,3,4,56,6,7,4,2}
# print(a)


# b=hash("hello")
# print(b)


# d={1:"hello",2:56}
# print(type(d))


# # list practice questions
# neg=0
# pos=0
# l = [1, -2, 3, -4, 5]
# for i in range(len(l)):
#     if l[i]<0:
#         neg+=1
#     else:
#         pos+=1
# print(f" totak - + are {neg},{pos}")

# l = [1, -2, 3, -4, 5]
# sum=0

# for i in range(len(l)):
#     sum+=l[i]
# avg=sum/len(l)
# print(f"sum is {sum} and the average is {avg}")

# l = [1, -2, 3, -4, 5]
# min=l[0]
# max=l[0]

# for i in range(len(l)):
#     if l[i]>max:
#         max=l[i]
#     if l[i]<min:
#      min=l[i]
# print(f"max={max},min={min}")
 
# l = [1, -2, 3, -4, 5]
# even=[]
# odd=[]
# for i in range(len(l)):
#     if l[i]%2==0:
#         even.append(l[i])
#     else:
#         odd.append(l[i])
# print(f"even no are {even}, odd are {odd}")

# l = [1, -2, 3, -4, 5]
# firstmax=l[0]
# secondmax=l[0]
# thirdmax=l[0]
# for i in range(len(l)):
#     if l[i]>firstmax:
#         thirdmax=secondmax
#         secondmax=firstmax
#         firstmax=l[i]
#     elif l[i]>secondmax:
#         secondmax=l[i]
#     else:
#         thirdmax=l[i]
# print(f"{firstmax},{secondmax},{thirdmax}")


# l=[1,2,3,4,4]
# k=1
# for i in range(1,len(l)):
#     if l[i]!=l[k-1]:
#         l[k]=l[i]
#         k+=1
#     else:
#         l.remove(l[i])
# print(f"{l}")
    
# l=[1,2,3,4,4]
# # s[0]=0
# n=len(l)
# for i in range(len(l)//2):
#     s=l[i]
#     l[i]=l[n-i-1]
#     l[n-i-1]=s
# print(l)


# l=[1,2,3,1,2,3,4]
# a=0
# for i in range (len(l)-1):
#     if l[i]<l[i+1]:
#         a+=1
#     else:
#         a=1
# print(f"largest incresing {a}")

# l = [1,2,3,4,5]
# cf=l[0]
# for i in range (1,len(l)):
#     cf=l[i-1]
#     l[i]=l[i]+cf
# print(f"{l}")                


# l=[1,2,3,4,5]
# k=len(l)-1
# for i in range((len(l)-1)//2):
#     s=l[i]
#     l[i]=l[k-i-1]
#     l[k-i-1]=s
     
# print(f"{l}")
# n=len(l)
# for i in range((len(l))//2):
#     t=l[i]
#     l[i]=l[n-i-1]
#     l[n-i-1]=t
# print(f"{l}")


# tuple questions
# t = (1, 2, 3, 4, 5)
# sum=0
# for i in range(len(t)):
#     sum+=t[i]
# print(f"{sum}")
# n=len(t)
# s=()
# for i in range(len(t)-1,-1,-1):
#     s+=(t[i],)
   
# print(f"{s}")


# t = (1,2,3,4,5)

# new = (t[-1],) + t[1:-1] + (t[0],)

# print(new)

# t = (1,2,3,4,5,6,7)

# for num in t: prime
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=" ")


# t = (1,2,3,4) consecutive sum

# res = ()
# for i in range(len(t)-1):
#     res += (t[i] + t[i+1],)

# print(res)

# t = (1,2,3,4)
# r=();
# # tuple immutable not change new bannan padega
# for i in range(len(t)-1):
#     r+=(t[i]*t[i+1],)
#     # append aese honge boss
# print(f"{r}")


# t = (10,20,30)

# res = ()
# for i in range(len(t)):
#     res += ((i, t[i]),)

# print(res)

# setttttttttttttt
# l = [1,2,2,3,4,4,5]
# s = set(l)
# print(s)
# a = {1,2,3,4}
# b = {3,4,5,6}
# print(a & b)
# print(a | b)
# print(a ^ b)  

# vowels = {'a','e','i','o','u'}
# res = set()

# for i in s://traversal aese hi honga range krke nahi honga 
#     if i in vowels:
#         res.add(i)

# print(len(res))



# res = []
# for i in l:
#     if i not in res:
#         res.append(i)

# print(res)



# d1 = {"a":1, "b":2}
# d2 = {"c":3, "d":4}

# res = {}

# for i in d1:
#     res[i] = d1[i]

# for i in d2:
#     res[i] = d2[i]

# print(res)

# d = {"a":10, "b":20, "c":30}

# total = 0

# for i in d:
#     total += d[i]

# print(total)

# l = [1,2,2,3,3,3,4]

# freq = {}

# for i in l:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq)


# d1 = {"a":10, "b":20}
# d2 = {"a":5, "c":15}

# res = {}

# # pehle d1 copy
# for i in d1:
#     res[i] = d1[i]

# # d2 add karo
# for i in d2:
#     if i in res:
#         res[i] += d2[i]
#     else:
#         res[i] = d2[i]

# print(res)

# a=[1,1,1,1,2,2,3,4,5,5,6]
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
# dictionary ka use frequenct mein use hota hain boss


# d1={10:100,20:200,30:300}
# d2={30:300,40:400,50:500}
# for i in d2:
#     if i in d1.keys():
#         d1[i]+=d2[i]
#     else:
#         d1[i]=d2[i]
# print(d1)
# dhyan se concept samjho boss