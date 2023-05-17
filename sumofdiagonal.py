# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))
# first_diagonal = 0
# for i in range(n): #i=0 ,i=1
#     first_diagonal+=arr[i][i] #arr[0][0]=1, arr[1][1]=5
# second_diagonal = 0
# for i in range(n): #i=0,0,0 ... 1,1,1... 2,2,2
#     for j in range(n): #j=0,1,2... 0,1,2 ... 0,1,2
#         if i + j == n - 1:  #,, 0+1=2,,0+2=2,, 1+0=2,, 1+1=2,, 2+0=2
#             second_diagonal += arr[i][j] #arr[1][1]=5 arr[0][2]=3 arr[2][0]=6
# sum_of_both_diagonal=first_diagonal+second_diagonal
# print(sum_of_both_diagonal)

n=int(input())
for i in range(n):
    for j in range(n):
        print(i,n)