class Solution:
  def checkPerfectNumber(self, num: int) -> bool:
    if num <= 0:
      return False
    if num == 1:
      return True
    xsum = 0
    for i in range(1, num + 1):
      i2 = i * i
      if i2 < num:
        if num % i == 0:
          xsum += i + num // i
      elif i2 == num:
        xsum += i
      else:
        break
    return xsum == num * 2

class Solution:
  def __init__(self):
    # Euclid-Euler Theorem:
    # 2^(p−1)*(2^p−1) is an even perfect number whenever 2^p−1 is prime, where p is prime.
    # Mersenne primes: prime numbers of the form 2^p − 1, a necessary but not sufficiency condition is p must be prime,
    # say 2^2 - 1 = 3, but 2^11 - 1 = 2047 = 23 * 89 is not prime, so not condition is not sufficiency.
    # For num <= 10^8, only need to consider p = 2,3,5,7,13,17,19,31
    self.perfect = set([])
    for p in [2,3,5,7,13,17,19,31]:
      self.perfect.add((1 << (p - 1)) * ((1 << p) - 1))
  def checkPerfectNumber(self, num: int) -> bool:
    return num in self.perfect

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 4, 5, 6, 7, 8, 28, 42, 85
  ]
  rslts = [solver.checkPerfectNumber(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
