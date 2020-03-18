from collections import Counter

class Solution:
  def removeDuplicateLetters(self, s: str) -> str:
    """greedy approach: smallest leftmost with every other character appeared once on right, recursive.
    """
    cntr = Counter(s)
    h = 0
    for i, x in enumerate(s):
      if x < s[h]:
        h = i
      cntr[x] -= 1
      if cntr[x] == 0:
        break
    return s[h] + self.removeDuplicateLetters(s[(h + 1):].replace(s[h], "")) if s else ''

class Solution:
  def removeDuplicateLetters(self, s: str) -> str:
    """greedy approach: smallest leftmost with every other character appeared once on right, stack.
    """
    cntr = Counter(s)
    stack, seen = [], set([])
    for x in s:
      if x not in seen:
        # x should be placed ealier
        while stack and x < stack[-1] and cntr[stack[-1]] > 0:
          seen.remove(stack.pop())
        stack.append(x)
        seen.add(x)
      cntr[x] -= 1
    return ''.join(stack)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "acbcb",
    "abacb",
    "bcabc",
    "ecbacba",
    "cdadabcc",
    "leetcode",
  ]
  rslts = [solver.removeDuplicateLetters(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")