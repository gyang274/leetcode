from typing import List
from collections import deque

class Solution:
  def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    # simulation O(2n)
    n = len(deck)
    index, ans = deque(range(n)), [None] * n
    for card in sorted(deck):
      # put card in order
      ans[index.popleft()] = card
      # move card to ende
      if index:
        index.append(index.popleft())
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [17,13,11,2,3,5,7],
  ]
  rslts = [solver.deckRevealedIncreasing(deck) for deck in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
