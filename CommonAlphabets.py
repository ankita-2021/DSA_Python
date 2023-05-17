from collections import Counter
n=int(input())
arr=input()
count1=Counter(arr)
for i in range(n-1):
    arr=input()
    count2=Counter(arr)
    for j in count1:
        count1[j]=min(count1[j],count2[j])
for i in sorted(count1.keys()):
    if count1[i]>0:
        print(i, count1[i])



