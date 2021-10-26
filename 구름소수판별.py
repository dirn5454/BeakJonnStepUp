import math
n = int(input())
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 :
            return False
    return True
result = isPrime(n) 
print(result)