# # method1 import default dict

# from collections import Counter
# k=int(input())
# names=input().split()
# count=Counter(names)
# res=[]
# for (key,values) in count.items():
#     if values>k:
#         res.append(key)
# res.sort()
# if len(res)<=0:
# 	print("no such names in this town!!!")
# else:
# 	for i in res:
# 		print(i)

# # method2 create a dict own

# k=int(input())
# names=input().split(" ")
# d={}
# for i in names:
# 	if i in d:
# 		d[i]=d[i]+1
# 	else:
# 		d[i]=1
# res=[]
# for key,values in d.items():
# 	if k<values:
# 		res.append(key)
# res.sort()
# if len(res)<=0:
# 	print("no such names in this town!!!")
# else:
# 	for i in res:
# 		print(i)


