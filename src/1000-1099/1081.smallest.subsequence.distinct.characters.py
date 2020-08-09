from collections import Counter

class Solution:
  def smallestSubsequence(self, text: str) -> str:
    # stack
    stack, seen, d = [], set(), Counter(text)
    for x in text:
      if x not in seen:
        # put x in front to make ans as small as possible
        while stack and stack[-1] > x and d[stack[-1]] > 0:
          seen.remove(stack.pop())
        stack.append(x)
        seen.add(x)
      d[x] -= 1
    return ''.join(stack)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "leetcode",
    "cdadabcc",
    "bcbcbcababa",
  ]
  rslts = [solver.smallestSubsequence(text) for text in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
