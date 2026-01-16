'''
Date:->15 Jan 2026
Here in this question there are N number of books
and each book has A[i] number of pages and we have to allocate
these books to M number of students so that the maximum number
of pages allocated to a student is minimum

Three conditions must be followed
1. each book should be allocated to a student
2. Each student has to be allocated at least one book
3. Allotment should be in contiguous order

calculate and return that minimum possible number

Return -1 if a valid assignment is not possible 
'''
def is_Valid(arr,n,m,maxAllowedPages):
    stu, pages = 1,0
    for i in range(n):              # O(n)
        if arr[i] > maxAllowedPages:
            return False
        if pages+arr[i] <= maxAllowedPages:
            pages+= arr[i]
        else:
            stu += 1
            pages = arr[i]
    if stu > m:
        return False
    else:
        return True

def bookAllocation(arr,n,m):
    if m > n:
        return -1
    
    sum = 0
    for i in range(n): # O(n)
        sum += arr[i] 
    
    ans = -1
    st, end = 0,sum

    while st<= end:          # O(logN*n)
        mid = st+(end-st)//2

        if is_Valid(arr,n,m,mid):
            ans = mid
            end = mid-1
        else:
            st = mid+1
    return ans

arr = [15,17,20]
n = len(arr)
m = 2
print(bookAllocation(arr,n,m))





