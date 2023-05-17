# correct solution...
# N,Q=[int(x) for x in input().split()]
# Time=list(map(int,input().split()))
# score=list(map(int,input().split()))

# Time.sort(reverse=True)
# score.sort(reverse=True)

# required_time=[Time[0]]
# for i in range(1,N):
#     needed_time=Time[i]+required_time[i-1]
#     required_time.append(needed_time)
# for i in range(Q):
#     K=int(input())
#     print(required_time[K-1])

# n=int(input())
# nums=[int(x) for x in input().split()]
# for i in range(0,2*n,2):
#     pr
        

'''def count_roataion_liner(nums):
    n=len(nums)
    start=0
    end=n-1
    while start<=end:
        mid=start+(end-start)//2
        prev = (mid-1+n)%n
        nex = (mid+1)%n
        if nums[mid]<nums[prev] and nums[mid]<=nums[nex]:
            return mid
        elif nums[mid]<nums[start]: end = mid-1
        elif nums[mid]>nums[end]: start = mid+1
        else: return 0
nums=list(map(int,input().split()))
n=len(nums)
print(count_roataion_liner(nums))'''


