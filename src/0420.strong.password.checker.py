class Solution:
  def strongPasswordChecker(self, s: str) -> int:
    # a-z A-Z 0-9
    missing_type = 3
    if any('a' <= c <= 'z' for c in s):
      missing_type -= 1
    if any('A' <= c <= 'Z' for c in s):
      missing_type -= 1
    if any(c.isdigit() for c in s):
      missing_type -= 1
    # no more than 3
    replace = 0
    # xxx need one replace, but also can be achieved by delete one
    # xxxx need one replace, but also can be achieved by delete two
    # xxxxx need one replace, but also can be achieved by delete three
    r0, r1 = 0, 0
    i = 2
    while i < len(s):
      if s[i] == s[i - 1] == s[i - 2]:
        length = 2
        while i < len(s) and s[i] == s[i - 1]:
          length += 1
          i += 1
        replace += length // 3
        if length % 3 == 0:
          r0 += 1
        elif length % 3 == 1:
          r1 += 1
      else:
        i += 1
    # key: if len(s) > 20, use delete to proxy replace to minimize change needed..
    if len(s) < 6:
      return max(missing_type, 6 - len(s))
    elif len(s) < 20:
      return max(missing_type, replace)
    else:
      delete = len(s) - 20
      # use delete to proxy replace: xxx
      replace -= min(delete, r0)
      # use delete to proxy replace: xxxx
      replace -= min(max((delete - r0) // 2, 0), r1)
      # use delete to proxy replace: xxxxx (or say delete xxx at all)
      replace -= max((delete - r0 - 2 * r1) // 3, 0)
    return delete + max(missing_type, replace)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "aabbccdd",
    "1111111111",
  ]
  rslts = [solver.strongPasswordChecker(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")