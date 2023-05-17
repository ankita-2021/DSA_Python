# Python program to interchange first and last elements in a list

# Approch 1
''''n=int(input())
l1=list(map(int,input().split()))
l1[0],l1[-1]=l1[-1],l1[0]
print(l1)'''

# Approch 2
''''n=int(input())
l1=list(map(int,input().split()))
size = len(l1)
temp=l1[0]
l1[0]=l1[size-1]
l1[size-1]=temp
print(l1)'''

# Check if element exists in list in Python
''''n=[int(x) for x in input().split()]
l1=[int(x) for x in input().split()]
temp=int(input())
for i in l1:
    if i==temp:
        print("exist")
        break
else:
    print("not")'''

# n=int(input())
# for _ in range(n):
#     M,S=map(int,input().split())
#     if S>M:
#         print(0)
#     else:
#         listen=M//S
#         print(listen)
'''
n=int(input())
res=[]
for i in range(1,11):
    if n%i==0:
        res.append(i)
print(max(res))'''

# n=[int(x) for x in input().split()]
# l1=[int(x) for x in input().split()]
# summ=0
# for i in l1:
#     summ=summ+i
# print(summ)

'''arr=list(map(int,input().split()))
arr.sort()
mini=sum(arr[0:4])
maxi=sum(arr[1:5])
print(f'{mini} {maxi}')'''

# a = input().strip().split(' ')
# for i in range(0, len(a)):
#     a[i] = int(a[i])
    
# s = sum(a)
# print(str(s - max(a)) + " " + str(s - min(a)))


# t=int(input())
# for _ in range(t):
#     n=[int(x) for x in input().split()]
#     s=input()
#     for i in range(len(s)-1):
#         s[i],s[i+1]=s[i+1],s[i]
#     print(s)

# count=0
# for i in arr:
#     mx=max(arr)
#     if i==mx:
#         count+=1
# print(count)
'''arr=list(map(int,input().split()))
s=len(arr)
if s%2!=0:
    s=s-1
for i in range(0,s,2):
    arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)'''