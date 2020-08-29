class Solution:
  def reverseParentheses(self, s: str) -> str:
    # O(N), one pass, stack
    # p: num of '(' seen - num of ')' seen
    p, prev, curr = 0, [], []
    for x in s:
      if x == '(':
        curr.append([])
        prev.append(curr)
        curr = curr[-1]
        p += 1
      elif x == ')':
        if p & 1:
          z = ''.join(reversed(curr))
        else:
          z = ''.join(curr)
        curr = prev.pop()
        curr.pop()
        curr.append(z)
        p -= 1
      else:
        curr.append(x)
    return ''.join(curr)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "(abcd)",
    "(u(love)i)",
    "(ed(et(oc))el)",
    "a(bcdefghijkl(mno)p)q",
    "ta()usw((((a))))"
  ]
  rslts = [solver.reverseParentheses(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
