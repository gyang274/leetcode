class Solution:
  def minimumDeletions(self, s: str) -> int:
    n, la, rb = len(s), 0, s.count('b')
    # min deletion <=> max length of kept a..ab..b
    m = rb
    for i in range(n):
      if s[i] == 'a':
        la += 1
      else:
        rb -= 1
      m = max(m, la + nb)
    return n - m
