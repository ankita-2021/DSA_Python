n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
fold_arr=int(input())
while(fold_arr>0):
    res=[0]*(len(arr)//2)
    for i in range(len(arr)//2):
        res[i]=arr[i]+arr[-i-1]
    if len(arr)%2!=0:
        res.append(arr[len(arr)//2])
    arr=res
    fold_arr-=1
print(len(arr))
for i in arr:
    print(i)
