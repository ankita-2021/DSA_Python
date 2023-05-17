arr=list(map(str,input().split()))  #right code h bs yha input run nhi horha
maxx=0
for i in arr:
    words=i.split(' ')
    if len(words)>maxx:
        maxx=len(words)
print(maxx)
