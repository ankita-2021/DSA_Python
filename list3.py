# Diagonal element difference
'''n=int(input())
arr=[[int(x) for x in input().split()] for j in range(n)]
d1, d2=0,0
for i in range(n):
    for j in range(n):
        if i==j:
            d1+=arr[i][j]
        if i+j==n-1:
            d2+=arr[i][j]
diff=abs(d1-d2)
print(diff)'''

'''n=int(input())
for _ in range(n):
    x,y,a,b,k=map(int,input().split())
    i=1
    while(i<=k):
        a=a+x
        b=b+y 
        i=i+1
    if a<b:
        print("PETROL")
    elif b<a:
        print("DIESEL")
    else:
        print("SAME PRICE")'''

# tc=int(input())
# for _ in range(tc):
#     n,x,y=map(int,input().split())
#     s=input()
#     count1=0
#     count2=0
#     for i in s:
#         if i=="0":
#             count1+=1
#         elif i=="1":
#             count2+=1
#     tax=min(x,y)
#     print(tax)
'''n=int(input())
for _ in range(n):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    res=[]
    for i in arr:
        if i<=k:
            res.append("1")
            k=k-i
        else:
            res.append("0")
    print("".join(res))'''
# n=int(input())
# for _ in range(n):
#     dsa1,toc1,dm1=list(map(int,input().split()))
#     dsa2,toc2,dm2=list(map(int,input().split()))
#     if (dsa1+toc1+dm1)>(dsa2+toc2+dm2):
#         print("Dragon")
#     elif (dsa1+toc1+dm1)<(dsa2+toc2+dm2):
#         print("Sloth")
#     if (dsa1+toc1+dm1)==(dsa2+toc2+dm2):
#         if dsa1==dsa2:
#             if toc1==toc2:
#                 if dm1==dm2:
#                     print("Tie")
#                 elif dm1>dm2:
#                     print("Dragon")
#                 else:
#                     print("Sloth")
#             if toc1>toc2:
#                 print("Dragon")
#             elif toc1<toc2:
#                 print("Sloth")
#         elif dsa1>dsa2:
#             print("Dragon")
#         else:
#             print("Sloth")
            
'''n=int(input())
for _ in range(n):
    n,p,x,y=map(int,input().split())
    arr=list(map(int,input().split()))
    time=0
    for i in range(0,p):
        if arr[i]==1:
            time+=y
        elif arr[i]==0:
            time+=x
    print(time)'''
    
# tc=int(input())
# for _ in range(tc):
#     n=int(input())
#     d=[int(i) for i in input().split()]
#     print(len(set(d)))
# def last_char(s):
#     return s[-1]
# s=input()
# print(last_char(s))

'''def sumMulti(arr,n):
    total=0
    for i in arr:
        if i%n==0:
            total+=i
    return total
arr=map(int,input().split())
n=int(input())
print(sumMulti(arr, n))'''

# def swap(a,b):
#     a,b=b,a
#     return a,b
# a=int(input())
# b=int(input())
# a,b=swap(a, b)
# print(a)
# print(b)

'''def college(n):
    summ=0
    for i in range(1,n+1):
        if n%i==0:
            summ+=i
    return summ
n=int(input())
print(college(n))'''

# arr = list(map(int,input().split()))
# def difference_sum_even_odd_index(arr):
# 	even_sum=0
# 	odd_sum=0
# 	for i in range(0,len(arr)):
# 		if i%2==0:
# 			even_sum=even_sum+arr[i]
# 		else:
# 			odd_sum=odd_sum+arr[i]
# 	return even_sum-odd_sum
# print(difference_sum_even_odd_index(arr))

'''n=int(input())
prod=1
for i in range(1,n+1):
    prod=prod*i
print(prod)'''
# def convertTime(self, current: str, correct: str) -> int:
#         # 1. convert both the current and correct times to integers in terms of minutes
#         current = int(current[0:2]) * 60 + int(current[3:5])
#         correct = int(correct[0:2]) * 60 + int(correct[3:5])
        
#         # 2. set up a times array and an answer variable
#         times = [60, 15, 5, 1]
#         answer = 0
        
#         # 3. while current != correct, go thru the times in descending order, adding the first time that fits until current == correct, increasing the answer by 1 for each addition
#         while current != correct:
#             for time in times:
#                 if current + time <= correct:
#                     current += time
#                     answer += 1
#                     break
        
#         # 4. return the answer
#         return answer


# swaping present and next ele
# val=eval(input("Enter a list "))
# print("Original List is:",val)
# s=len(val)
# if s%2!=0:
#     s=s-1
# for i in range(0,s,2):
#     val[i],val[i+1]=val[i+1],val[i]
# print("List after swapping :",val)
