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