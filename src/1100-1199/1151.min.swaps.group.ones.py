from typing import List

class Solution:
  def minSwaps(self, data: List[int]) -> int:
    # O(N), two pass, x = sum(data), min num of swap = x - max(sum of subarray length x)
    x, n = sum(data), len(data)
    y = k = sum(data[:x])
    for i in range(x, n):
      k += data[i] - data[i - x]
      y = max(y, k)
    return x - y

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0,1,0,0,0],
    [1,0,1,0,1],
    [1,0,1,0,1,0,0,1,1,0,1],
  ]
  rslts = [solver.minSwaps(data) for data in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
