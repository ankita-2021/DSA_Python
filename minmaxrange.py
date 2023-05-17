# s=input()
# n=int(input())
# res=[]
# for i in range(n):
#     res.append(s)
# print(res)

# def swap(a,b):
#     a,b=b,a
#     return a,b
# a=int(input())
# b=int(input())
# print(swap(a, b))

''''def differenceOfSumOfEvenOddIndexnumbers(arr):
    esum=0
    osum=0
    for i in range(0,len(arr)):
        if i%2==0:
            esum+=arr[i]
        else:
            osum+=arr[i]
    return esum-osum
arr=list(map(int,input().split()))
print(differenceOfSumOfEvenOddIndexnumbers(arr))'''

# n=int(input())
# for i in range(1,n+1):
# 	for j in range(1,(n-i)+1):
# 		print(" ", end="")
# 	for ladder in range(1,i+1):
# 		print("#",end="")
# 	print()

# arr=list(map(int,input().split()))
# matrix=[]
# for i in range(len(arr)):
#     if i%2==0:
#         matrix.append(len(arr[i])//2)
# print(matrix)


def build_matrix(rows, cols):
    matrix = []

    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])

    return matrix

# if __name__ == '__main__':
print(build_matrix(6, 10))