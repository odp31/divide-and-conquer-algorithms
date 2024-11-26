# recursive algorithm for multiplying large integers more efficiently than the 
# traditional grade-school multiplicatoin method
# based on D AND C

def karatsuba(x, y):
  """ multiples two integers using the karatsuba algorithm """
  if x < 10 or y < 10:
    return x * y
  # determine length of larger number
  n = max(len(str(x)), len(str(y)))
  
  # divide numbers into two havles
  n_half = n // 2
  a, b = divmod(x, 10**n_half)
  c, d = divmod(y, 10**n_half)

  #recursively calculate products 
  ac = karatsuba(a, c)
  bd = karatsuba(b, d)
  ad_bc = karatsuba(a + b, c + d) - ac - bd

  # combine results
  product = ac * 10**(2*n_half) + (ad_bc * 10**n_half) + bd
  return product

# example usage
x = 12345
y = 67890
result = karatsuba(x, y)
print(result) 
