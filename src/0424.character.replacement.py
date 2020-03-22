from collections import defaultdict

class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    """slide window with two pointers
    """
    xmax, i, j, d, ms, mx = 0, 0, 0, defaultdict(lambda: 0), set([]), 0
    while j < len(s):
      if len(d) == 0 or s[j] in ms or j - i - mx < k:
        d[s[j]] += 1
        if d[s[j]] > mx:
          mx = d[s[j]]
          ms = {s[j]}
        elif d[s[j]] == mx:
          ms.add(s[j])
        j += 1
        xmax = max(xmax, j - i)
      else:
        d[s[i]] -= 1
        if d[s[i]] == 0:
          d.pop(s[i])
          if not d:
            mx = 0
            ms = set([])
        if s[i] in ms:
          mx = max(d.values())
          ms = {k for k in d if d[k] == mx}
        i += 1
      # xmax = max(xmax, j - i)
      # print(f"{i=}, {j=}, {d=}, {ms=}, {mx=}, {xmax=}")
    return xmax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("ABAB", 0),
    ("ABAB", 1),
    ("AABBABA", 1),
    ("AABBABA", 2),
    ("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4),
  ]
  rslts = [solver.characterReplacement(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")