class Solution:
  def removeDuplicates(self, s: str, k: int) -> str:
    # stack, Q1047
    stack, count = [], 0
    for x in s:
      if stack and stack[-1] == x:
        count += 1
      else:
        count  = 1
      stack.append(x)
      if count == k:
        stack, count = stack[:-k], 0
        if stack:
          z, count = stack[-1], 1
          while count <= len(stack) and stack[-count] == z:
            count += 1
          count -= 1
    return ''.join(stack)

class Solution:
  def removeDuplicates(self, s: str, k: int) -> str:
    # stack, stack of (x, counts), Q1047
    stack = []
    for x in s:
      if stack and stack[-1][0] == x:
        stack.append((x, stack[-1][1] + 1))
      else:
        stack.append((x, 1))
      if stack[-1][1] == k:
        stack = stack[:-k]
    return ''.join(x for x, count in stack)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcd", 2),
    ("deeedbbcccbdaa", 3),
    ("pbbcggttciiippooaais", 2),
  ]
  rslts = [solver.removeDuplicates(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
