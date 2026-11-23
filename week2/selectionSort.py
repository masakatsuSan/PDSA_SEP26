
def selectionSort(arr):
    n = len(arr)
    for  i in range(n):
        min = i 
        for j in range(i+1,n):
            if arr[j] < arr[min] :
                min = j 
        arr[i],arr[min] = arr[min],arr[i]
            
    return arr 


print(selectionSort([1,2,6,23,58,3,37,22]))