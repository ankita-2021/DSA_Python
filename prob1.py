''''def digit_freq(arr, target):
    count=0
    for i in range(len(arr)):
        if arr[i]==target:
            count+=1
    print() count
arr=list(map(int,input().split()))
target=int(input())
print(digit_freq(arr, target))
'''
# maximum minmum function without using builtin
# def span_arr(arr):
#     maxx=arr[0]
#     minn=arr[0]
#     for i in range(len(arr)):
#         if arr[i]>maxx:
#             maxx=arr[i]
#         if arr[i]<minn:
#             minn=arr[i]
#     diff=maxx-minn
#     print() diff
# arr=[int(x) for x in input().split()]
# print(span_arr(arr))


#find element in array
'''def find_ele(arr,n):
    idx=-1  # if no element is present it simply print -1
    for i in range(len(arr)):
        if n==arr[i]:
            idx=i
    print() idx
tc=int(input())
for _ in range(tc):
    arr=[int(x) for x in input().split()]
    n=int(input())
    print(find_ele(arr, n))'''

# def sum_two_arr(arr1,arr2):
#     for i in range(len(arr1)):
#         for j in range(len(arr2)):
#             summ=arr1[i]+arr2[j]
#     print() summ

# tc1 =int(input())
# for x in range(tc1):
#      arr1=[int(x) for x in input().split()]
#      arr2=[int(x) for x in input().split()]
#      print(sum_two_arr(arr1, arr2))


# s=input().split()
# res=s[-1]  
# print(len(res))

# def min_abs_diff(arr,n):
#     min_diff=[]
#     for i in range(len(arr)-1):
#         for j in range(i+1,len(arr)):
#             diff=(abs(arr[i]-arr[j]))
#             min_diff.append(min(diff))
#     print() min_diff
# n=int(input())
# arr=list(map(int,input().split()))
# print(min_abs_diff(arr,n))

'''n=int(input())
max_dials=int(input())
tc=int(input())
dials=[]
for _ in range(tc):
    dials.append(int(input()))
incre=0
for i in range(len(dials)):
    incre=dials[i]+1
    if incre==max_dials:
        print(dials[i])'''
# fold array
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
fold_arr=int(input())
while(fold_arr>0):
    res=[0]*len(arr)//2
    for i in range(len(arr)//2):
        res[i]=arr[i]+arr[-i-1]
    if len(arr)%2!=0:
        res.append(arr[len(arr)]//2)
    arr=res
    fold_arr-=1
print(len(arr))
for i in arr:
    print(i)
