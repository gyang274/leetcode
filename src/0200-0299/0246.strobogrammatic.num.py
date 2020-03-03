class Solution:
  def isStrobogrammatic(self, num: str) -> bool:
    stroboSelf = set(["0", "1", "8"])
    stroboPair = {"6": "9", "9": "6"}
    n = len(num)
    if n % 2 == 1 and num[n // 2] not in stroboSelf:
      return False
    i = 0
    while i < n // 2:
      condStroboSelf = (num[i] in stroboSelf and num[i] == num[n - 1 - i])
      condStroboPair = (num[i] in stroboPair and stroboPair[num[i]] == num[n - 1 - i])
      if not (condStroboSelf or condStroboPair):
        return False
      i += 1
    return True

class Solution:
  def isStrobogrammatic(self, num: str) -> bool:
    strobo = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
    i = 0
    for i in range((len(num) + 1) // 2):
      if not (num[i] in strobo and strobo[num[i]] == num[- (i + 1)]):
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "0", "1", "2", "3", "5", "8", "10", "11", "42", "69", "96", "101", "181", "609", "619", "689", "9696", "9966",
  ]
  rslts = [solver.isStrobogrammatic(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")