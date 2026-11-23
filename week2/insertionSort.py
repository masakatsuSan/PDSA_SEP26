def insertionSort(arr):
    n  = len(arr)
    for i in range(1,n):
        curr = arr[i]
        prev = i - 1
        while (prev >= 0 and arr[prev]>curr) :
            arr[prev+1] = arr[prev]
            prev -= 1 
        arr[prev+1] = curr 
        
        
    return arr 

arr = [67, 4, 2, 88, 1, 6]

print(insertionSort(arr))