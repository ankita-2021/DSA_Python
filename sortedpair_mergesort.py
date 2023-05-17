# tc=[int(x) for x in input().split()]
# arr=list(map(int,input().split()))
# n=len(arr)
# count=0
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]<=arr[j]:
#             count+=1
# print(count)

# inversion count=0
'''def inversion_count(arr,left,right):
    count=0
    if left<right:
        mid=(left+right)//2
        count+=inversion_count(arr, left, mid)
        count+ inversion_count(arr, mid+1, right)
        count+=merge_sort(arr, left, mid, right)
    return count
def merge_sort(arr, left,mid, right):
    sorted=[0]*(right-left+1)
    inv_count=0
    i=left
    j=mid+1
    k=0
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            sorted[k]=arr[i]
            inv_count+=(right-j+1)
            i+=1
        else:
            sorted[k]==arr[j]
            # inv_count+=(mid-i+1)
            j+=1
        k+=1
    while i<=mid:
        sorted[k]=arr[i]
        i+=1
        k+=1
    while j<=right:
        sorted[k]=arr[j]
        j+=1
        i+=1
    ptr=left
    for t in sorted:
        arr[ptr]=t
        ptr+=1
    return inv_count
n=[int(x) for x in input().split()]
arr=list(map(int,input().split()))
print(inversion_count(arr, 0, len(arr)-1))'''


# def merge(nums1, nums2):    
#     # List to store the results 
#     merged = []
    
#     # Indices for iteration
#     i, j = 0, 0
    
#     # Loop over the two lists
#     while i < len(nums1) and j < len(nums2):        
        
#         # Include the smaller element in the result and move to next element
#         if nums1[i] <= nums2[j]:
#             merged.append(nums1[i])
#             i += 1 
#         else:
#             merged.append(nums2[j])
#             j += 1
    
#     # Get the remaining parts
#     nums1_tail = nums1[i:]
#     nums2_tail = nums2[j:]
    
#     # Return the final merged array
#     return merged + nums1_tail + nums2_tail
# nums1=list(map(int,input().split()))
# nums2=list(map(int,input().split()))
# print(merge(nums1,nums2))



  





