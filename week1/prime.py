# check is the number is prime or not 
import math

def isprime(n):
    flag = True
    for i in range(2,n):
        if n%i == 0 :
            return False
    return flag

print(isprime(27))

# 36 --> 1,2,3,4,6,9,12,18,36

#count the factors 

def factors(n): #O(N)
    count = 0 
    for i in range(1,n+1):
        if n % i == 0 :
            count += 1 
    print(count)  
factors(103)