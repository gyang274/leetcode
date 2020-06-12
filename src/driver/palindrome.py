def isPalindrome(self, N: int) -> bool:
  s = str(N)
  n = len(s)
  if n & 1:
    x, m, y = s[:(n // 2)], s[n // 2], s[(n // 2 + 1):]
  else:
    x, y = s[:(n // 2)], s[(n // 2):]
  return x[::-1] == y

def nextPalindrome(self, N: int) -> int:
  # smallest palindrome integer > N.
  s = str(N)
  n = len(s)
  if n & 1:
    x, m, y = s[:(n // 2)], s[n // 2], s[(n // 2 + 1):]
    if x[::-1] > y:
      return int(x + m + x[::-1])
    elif m < '9':
      return int(x + str(int(m) + 1) + x[::-1])
    elif x < '9' * (n // 2):
      return int(str(int(x) + 1) + '0' + str(int(x) + 1)[::-1])
    else:
      return int('1' + '0' * (n - 1) + '1')
  else:
    x, y = s[:(n // 2)], s[(n // 2):]
    if x[::-1] > y:
      return int(x + x[::-1])
    elif x < '9' * (n // 2):
      return int(str(int(x) + 1) + str(int(x) + 1)[::-1])
    else:
      return int('1' + '0' * (n - 1) + '1')
