from collections import Counter

class Solution:
  def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    # O(26 * N) since minsize, maxsize <= 26
    d, i, n = Counter(), 0, len(s)
    while i < n:
      j, k, x = i, set(), ''
      while j < n and j - i < maxSize:
        x += s[j]
        k.add(s[j])
        j += 1
        if len(k) > maxLetters:
          break
        if j - i >= minSize:
          d[x] += 1
      i += 1
    return d.most_common()[0][1] if d else 0

class Solution:
  def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
    # O(N)
    # if a string have occurrences x times, any of its substring must appear at least x times.
    # so there must be a substring of length minSize, that has the most occurrences.
    # so we just need to count the occurrences of all substring with length minSize.
    count = Counter(s[i:(i + minSize)] for i in range(len(s) - minSize + 1))
    return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("aaaa", 1, 2, 3),
    ("aabcabcab", 2, 2, 3),
    ("aababcaab", 2, 3, 4),
  ]
  rslts = [solver.maxFreq(s, maxLetters, minSize, maxSize) for s, maxLetters, minSize, maxSize in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
