# from collections import Counter
# def luckynum(arr):
#     lst = []
#     x = Counter(arr)
#     for k,v in x.items():
#         if k==v:
#             lst.append(k)
                
#     if lst == [] :
#         return -1
#     else:
#         return min(lst)
# n=int(input())
# arr=[]
# for _ in range(n):
#     arr.append(int(input()))
# print(luckynum(arr))


# def lucky_num(arr):
#     dic={}
#     minval=0
#     for i in arr:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     for i in arr:
#         if dic[i]==i:
#             minval=max(minval, dic[i])
#     return minval
# n=int(input())
# arr=[]
# for _ in range(n):
#     arr.append(int(input()))
# print(lucky_num(arr))

'''img icons'''
# from collections import Counter
# def img_pixel(arr,icons):
#     x = Counter(arr)
#     for key,val in x.items():
#         if key==icons:
#             return val         
# n=int(input())
# arr=[]
# for _ in range(n):
#     arr.append(int(input()))
# pixel= int(input())
# for item in range(pixel):
#     icons=int(input())
# print(img_pixel(arr, icons))



