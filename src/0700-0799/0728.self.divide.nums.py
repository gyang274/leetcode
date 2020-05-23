class Solution:
  def isSelfDivide(self, num):
    for x in str(num):
      if x == "0" or num % int(x):
        return False
    return True
  def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    return [num for num in range(left, right + 1) if self.isSelfDivide(num)]
 