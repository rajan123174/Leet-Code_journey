# this is an Iterative code
def binarySearch(arr,target):
    start = 0  
    end = len(arr)

    while start <= end :
        mid = start +(end - start)//2

        if target > arr[mid]:
            start = mid+1
        elif target < arr[mid]:
            end = mid-1
        else:
            return mid
    return -1

arr = [-1,0,3,4,5,9,12]
target = 12

print(binarySearch(arr,target))

#Recursive method for binary search
start = 0
end = len(arr)
def recursive_binarySearch(arr,target,start,end):
    mid = start + (end-start)//2
    if start <= end:
        if target > arr[mid] :
            return recursive_binarySearch(arr,target,mid+1,end)#2nd half
        elif target < arr[mid]:
            recursive_binarySearch(arr,target,start,mid-1)#1st half
        else:
            return mid # target == mid
    return -1

print(recursive_binarySearch(arr,target,start,end))




    


