# # l1=[]

# # l2=[4, 7, 8, 2, 1, 3, 1, 7, 8]
# # # for i in range(len(l2)):
# # #     if i%2==0:
# # #         l1.append(l2[i])
# # for i in range(len(l2)-1,0,-1):
# #     l1.append(l2[i])

# # print(l1)

# # l1=list(map(int,input().split()))
# l1=[1,2,3,4,5,6]
# for i in range(len(l1)-1):
#     if i%2!=0:
#         l1.pop(i)
# print(l1)
'''n=int(input())
nums=[]
for _ in range(n):
	nums.append(int(input()))
count=0
temp=int(input())
for i in range(len(nums)):
	if nums[i]==temp:
		count+=1
print(count)
'''

# t=int(input())
# nums=list(map(int,input().split()))
# summ=0
# for i in range(t):
#     if nums[i]%2==0:
#         summ=summ+nums[i]
# print(summ)

# t=int(input())
# nums=list(map(int,input().split()))
# diff=float('inf')
# for i in range(len(nums)-1):
#     for j in range(i+1,len(nums)):
#         if abs(nums[i]-nums[j])<diff:
#             diff=abs(nums[i]-nums[j])
# print(diff)
# n=int(input())
# nums=list(map(int,input().split()))
# summ=0
# for i in range(len(nums)):
#     if i%2==0:
#         summ=summ+nums[i]
# print(summ)

# n=int(input())
# nums=list(map(int,input().split()))
# min_diff=[]
# for i in range(n-1):
#     for j in range(i+1,n):
#         diff=abs(nums[i]-nums[j])
#         min_diff.append(diff)
# print(min(min_diff))

'''n=int(input())
nums=[]
for _ in range(n):
	nums.append(int(input()))
for i in nums:
	count=0
	for j in nums:
		if nums[i]<nums[j]:
			count+=1
	if count==nums[i]:
		print(1)
		break
else:
	print(-1)'''
# max diff between incre ele
# nums=list(map(int,input().split()))
# maxx_diff=-1
# minn_ele=nums[0]
# for i in range(1,len(nums)):
# 	if nums[i]-minn_ele>maxx_diff:
# 		maxx_diff=nums[i]-minn_ele
	
# 	if nums[i]<minn_ele:
# 		minn_ele=nums[i]
# if maxx_diff>0:
# 	print(maxx_diff)
# else:
# 	print(-1)
'''
x=input().split()
count_x=0
for ele in x:
	if ele=="x++"or ele=="++x":
		count_x+=1
	elif ele=="x--" or ele=="--x":
		count_x-=1
print(count_x)'''

# nums =list(map(int,input().split()))
# k=int(input())
# count=0
# for i in range(len(nums)-1):
# 	for j in range(i+1,len(nums)):
# 		if k==abs(nums[i]-nums[j]):
# 			count+=1
# print(count)

nums=list(map(int,input().split()))
# nums_max=max(nums)
# nums_max_idx=nums.index(nums_max)
for i in range(len(nums)):
	left_ele=sum(nums[:i])
	right_ele=sum(nums[i+1:])
	if left_ele==right_ele:
		print(i)
		break
else:
	print(-1)

