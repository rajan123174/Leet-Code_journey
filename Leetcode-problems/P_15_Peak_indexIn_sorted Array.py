def peakIndex(arr):
    start = 1
    end = len(arr)-2

    while start <= end:
        mid = start+(end-start)//2
        if arr[mid-1]<arr[mid]>arr[mid+1]:
            return mid
        if arr[mid-1]<arr[mid]:
            start = mid+1
        else:
            end = mid-1
arr = [0,3,8,9,10,5,2]
print(peakIndex(arr))