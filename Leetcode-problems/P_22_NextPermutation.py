'''
changes will be in place not create extra space
LeetCode 31
'''

def nextPermutation(A,n):
    piv = -1
    for i in range(n-2,0,-1):
        if A[i] < A[i+1]:
            piv = i
            break
    if piv == -1:
        i = 0
        j = n-1
        while i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    for i in range(n-1,0,-1):
        if A[i] > A[piv]:
            A[i], A[piv] = A[piv], A[i]
            break
    
    i = piv+1
    j = n-1

    while i <= j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    return A

A = [1,2,3]
n = len(A)

print(nextPermutation(A,n))

