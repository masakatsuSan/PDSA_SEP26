def linearSearch(L,target):
    for i in range(len(L)):
        if target == L[i] :
            return i 
    return False 
    
print(linearSearch([1,2,3,4,65,78,0],9))
print(linearSearch([1,2,3,4,65,78,0],78))