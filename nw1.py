def rajan_odd(arr,s):
	
	for i in range(0,s):
		count=0
		for j in range(0,s):
			if arr[i]==arr[j]:
				count+=1
		if count%2!=0:
			return arr[i]
	return -1
n=int(input())

arr=list(map(int,input().split()))
s=len(arr)
print(rajan_odd(arr,s))
            