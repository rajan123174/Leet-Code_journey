'''
A = [1,2,3,0,0,0], m = 3 B = [2,5,6], n= 3
'''

def mergeSortedArray(A,B,m,n):
    idx, i, j = m+n-1, m-1, n-1

    while i >= 0 and j>= 0:
        if A[i] >= B[j]:
            A[idx] = A[i]
            idx -= 1
            i -= 1
        else:
            A[idx] = B[j]
            idx -= 1
            j -= 1
    while j >= 0:
        A[idx] = B[j]
        idx -= 1
        j -= 1
    return A


A = [1,2,3,0,0,0] 
B = [2,5,6]
m = 3
n = 3
print(mergeSortedArray(A,B,m,n))

