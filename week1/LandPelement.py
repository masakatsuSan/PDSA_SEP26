# note : Write a function find_Min_Difference(L, P) that accepts a list L of integers and P (positive integer) where the size of L is greater than P. The task is to pick P different elements from the list L, where the difference between the maximum value and the minimum value in selected elements is minimum compared to other differences in possible subset of p elements. The function returns this minimum difference value.

#[3, 4, 1, 9, 56, 7, 9, 12]

"""
if we can just sort the element and then create a sub array for 5 , take it range ; 
slide to next window do the same
"""

def min_dff(L,p):
    L_sort = sorted(L)
    n = len(L)  #8 , 5 
    # loop for 5 elements --> n-p+1 --> 5 
    min_diff = float('inf')
    for i in range(n-p+1):
        diff = L_sort[i+p-1] -  L_sort[i]   #last element of that subarray - first element of that subarray 
        if diff < min_diff :
            min_diff = diff 
    return min_diff

L = eval(input().strip())
p = int(input())
print(min_dff(L,p))