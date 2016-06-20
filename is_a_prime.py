def is_prime(num):
  if num > 1:
      for i in range(2,num+1):
          if num % i == 0 and i != num:
              return False
      return True
  else:
      return False
