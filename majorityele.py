'''from collections import Counter
def majority(arr):
    count=Counter(arr)
    size=len(arr)
    for (key,value) in count.items():
        if value>(size/2):
            print(key)
            return
    return "none"
arr=list(map(int,input().split()))
print(majority(arr))'''

