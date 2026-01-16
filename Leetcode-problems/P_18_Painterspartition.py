'''
Date:->15 Jan 2026
This is a classical problem of book allocation problem

Given N boards of length each given in form of array
and M painters such that each painter takes 1 unit of
time to paint all boards the constraints that :->
painters will only paint continuos section of boards
n = number of boards 
M = no of painters
task is t find minimum time to paint all boards
'''

def is_Possible(arr,n,m,maxAllowedTime):
    painters, time = 1,0
    for i in range(n):
        if arr[i]>maxAllowedTime:
            return False
        if time + arr[i] <= maxAllowedTime:
            time += arr[i]
        else:
            painters += 1
            time = arr[i]
    if painters > m:
        return False
    else:
        return True
    
def minTimeToPaint(arr,m):
    st, end, ans,n = max(arr), sum(arr), -1,len(arr)
    while st <= end:
        mid = st+(end-st)//2
        if m>n :
            return -1
        
        if is_Possible(arr,n,m,mid):
            ans = mid
            end = mid-1
        else:
            st = mid+1
    return ans

arr = [40,30,10,20] 
m = 2
print(minTimeToPaint(arr,m))



