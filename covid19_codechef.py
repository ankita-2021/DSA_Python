# covid19 codechef
'''tc=int(input())
for _ in range(tc):
    n=int(input())
    arr=list(map(int,input().split()))
    res=[]
    count=1
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i]<=2:
            count+=1
        elif arr[i+1]-arr[i]>2:
            res.append(count)
            count=1
    res.append(count)
    print(min(res), max(res))'''