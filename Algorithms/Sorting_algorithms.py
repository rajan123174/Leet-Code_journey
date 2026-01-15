'''
1. Bubble sort :->
steps:-
i. (n-1) iterations
ii. compare adjacent elements
iii. Lrger last me push karenge:- swap with previous
'''
# Bubble Sort
arr = [4,1,5,2,3]
def bubbleSort(arr):
    for i in range(len(arr)-1):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swap = True
        if swap is not True: # Array is already sorted
            return arr
    return arr
print(bubbleSort(arr))


'''
2. selection sort :->
intuition we will assume 
0th index is smallest 
1 part is sorted and another is unsorted 
then we swap smallest idx element with the first
element of unsorted sorted array
'''
def selectioSort(arr):
    for i in range(len(arr)-1):
        smallIdx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[smallIdx]:
                smallIdx = j
        arr[i],arr[smallIdx] = arr[smallIdx],arr[i]
        return arr
print(selectioSort(arr))

'''
3 . Insertion sort
'''
# Insertion sort
def insertionSort(arr):
    for i in range(1,len(arr)):
        curr = arr[i]
        prev = arr[i-1]
        while prev >= 0 and arr[prev] > curr:
            arr[prev+1] = arr[prev]
            prev -= 1
        arr[prev+1] = curr
        return arr
print(insertionSort(arr))
