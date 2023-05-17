


'''arr=[]
for i in range(int(input())):
    arr.append(int(input()))
res=[]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            break
        if j==(len(arr)-1):
            res.append(arr[i])
res.append(arr[len(arr)-1])
for i in range(len(res)-1,-1,-1):
    print(res[i])'''