def binarySearch(arr,target,l,r):
    # --> this neeeds to ne sorted first 
    while (l <= r ):
        mid = (l+r)//2
        if arr[mid] == target :
            return mid 
        elif (arr[mid]>target):
            return binarySearch(arr,target,l,mid-1)
        else :
            return binarySearch(arr,target,mid+1,r)
    return -1
    
print(binarySearch([1,2,3,5,8,9],8,0,5))    