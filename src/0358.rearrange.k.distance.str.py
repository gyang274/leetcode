from collections import defaultdict, Counter

class Solution:
  def rearrangeString(self, s: str, k: int) -> str:
    if s == "" or k < 2:
      return s
    # x: character -> counts
    x = defaultdict(lambda: 0)
    for w in s:
      x[w] += 1
    # cntr: counts -> counts of counts
    cntr = Counter(x.values())
    # xmax: max count of any single character
    xmax = max(cntr.keys())
    if xmax > len(s) // k + 1:
      return ""
    # cntr[xmax]: num of single character with max counts
    elif xmax == len(s) // k + 1 and cntr[xmax] > len(s) % k:
      return ""
    else:
      y = sorted([[x[k], k] for k in x], key=lambda v: (-v[0], v[1]), reverse=True)
      if xmax == len(s) // k + 1:
        # j make sure the last list in r is length len(s) % k
        i, j, r = -1, 0, [[] for _ in range(xmax)]
        print(y)
        while y:
          n, w = y.pop()
          for _ in range(n):
            if i % xmax < len(s) // k:
              r[i % xmax].append(w)
            elif j < len(s) % k:
              j += 1
              r[i % xmax].append(w)
            else:
              i -= 1
              r[i % xmax].append(w)
            i -= 1
        print(r)
      else:
        i, r = 0, [[] for _ in range(xmax)]
        while y:
          n, w = y.pop()
          for _ in range(n):
            r[i % xmax].append(w)
            i += 1
    return "".join(["".join(q) for q in r])

# class Solution:
#   def rearrangeString(self, s, k):
#     n = len(s)
#     if not k: return s
#     count = Counter(s)
#     xmax = max(count.values())
#     if (xmax - 1) * k + list(count.values()).count(xmax) > len(s):
#       return ""
#     r = list(s)
#     i = (n - 1) % k
#     for c in sorted(count, key=lambda i: -count[i]):
#       for j in range(count[c]):
#         r[i] = c
#         i += k
#         if i >= n:
#           i = (i - 1) % k
#     return "".join(r)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("", 0),
    ("a", 1),
    ("aa", 1),
    ("aaabc", 2),
    ("aabbc", 2),
    ("aabbcc", 2),
    ("aabbcc", 3),
    ("aaabbcc", 3),
    ("aaadbbcc", 3),
    ("abcdabcdabdeac", 4),
    ("aaaabbccddeeff", 4),
  ]
  rslts = [solver.rearrangeString(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")