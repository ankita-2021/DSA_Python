def sum_of_multiple(arr,integer):
    summ=0
    for i in range(len(arr)):
        if arr[i]%integer==0:
            summ=summ+arr[i]
    return summ
n=int(input())
arr=[]
for _ in range(n):
	arr.append(int(input()))
integer=int(input())
print(sum_of_multiple(arr,integer))