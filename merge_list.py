num1=list(map(int,input().split()))
num2= list(map(int,input().split()))
merge_list=[]
for i in range(len(num1)):
    merge_list.append(num1[i])
for j in range(len(num2)):
    merge_list.append(num2[j])
print(merge_list)