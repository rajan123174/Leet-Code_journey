'''
Date:->15 Jan 2026
Assign C cows to N stalls such that min distance between
them is largest possible.
task is to return Largest minimum distance
n = 5 , arr = [1,2,8,4,9] C = 3
'''
def is_Possible(arr,n,c,minAllowedDist):
    arr.sort()
    cows, dist = 1,arr[0]
    for i in range(1,n):
        if arr[i] - dist >= minAllowedDist:
            cows += 1
            dist = arr[i]
        if cows == c:
            return True
    return False

def largestMinDist(arr,c):
    st ,end, ans, n = 1, max(arr)-min(arr), -1, len(arr)

    while st <= end:
        mid = st +(end-st)//2
        if is_Possible(arr,n,c,mid):
            ans = mid
            st = mid+1
        else:
            end = mid-1
    return ans

arr = [1,2,8,4,9]
c = 3
print(largestMinDist(arr,c))