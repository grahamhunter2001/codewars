def isPrime(num):
    for i in range(2,num+1):
        if num % i == 0:
          return True
    return False

def isPP(num):
    n = 2
    while n <= log(num, 2):
        if isPrime(n):
            for m in range(2,int(num**0.5)+1):
                if m**n == num:
                    return [m,n]
        n += 1
    return None
