class Solution:
  def myAtoi(self, strs: str) -> int:
    INT_MAX = 2 ** 31 -1
    INT_MIN = - 2 ** 31
    nums = {
      '0': 0,
      '1': 1,
      '2': 2,
      '3': 3,
      '4': 4,
      '5': 5,
      '6': 6,
      '7': 7,
      '8': 8,
      '9': 9,
    }
    sign = 1
    rslt = 0
    i = 0
    l = len(strs)
    while (i < l and strs[i] == ' '):
      i += 1
    if (i < l and (strs[i] == '+' or strs[i] == '-')):
      sign = 1 if strs[i] == '+' else -1
      i += 1
    while (i < l and strs[i] in nums):
      if ((rslt > INT_MAX // 10) or (rslt == INT_MAX // 10 and nums[strs[i]] > 7)):
        if sign > 0:
          return INT_MAX
        else:
          return INT_MIN
      else:
        rslt = rslt * 10 + nums[strs[i]]
      i += 1
    return sign * rslt


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "42",
    "    -42",
    "4172 with words",
    "words with 4172",
    "-91283472332",
    "   +",
    "   +0 123",
    "+1",
    "++1",
    "--1",
    "+-1",
    "-+1",
    "   ",
    "",
  ]
  rslts = [solver.myAtoi(x) for x in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")