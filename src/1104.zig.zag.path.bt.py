from typing import List

class Solution:
  def pathInZigZagTree(self, label: int) -> List[int]:
    # path as complete binary tree
    # say, 26 -> [26, 13, 6, 3, 1]
    #             _____________1_____________              
    #            /                           \             
    #       _____2______               ______3______       
    #      /            \             /             \      
    #    __4__        __5___        __6___        __7___   
    #   /     \      /      \      /      \      /      \  
    #   8_    9_    10_    11_    12_    13_    14_    15_ 
    #  /  \  /  \  /   \  /   \  /   \  /   \  /   \  /   \
    # 16 17 18 19 20  21 22  23 24  25 26  27 28  29 30  31
    x, ans = label, []
    while x:
      ans.append(x)
      x //= 2
    ans = ans[::-1]
    # make the zig-zag path by revert every other level from bottom
    # so, how to flip to make it zig-zag? 
    # f(k) = (2^L +  2^(L + 1) - 1) - k, k is the value to flip, f(k) is the flipped value, and L is the level of node k
    #               _____________1_____________            
    #              /                           \           
    #        ______3______               ______2_____        flip: 3 -> 2, because f(k) = (2 + 3) - k = (2^1 + 2^2 - 1) = (2^0 * 3 - 1) - k, k = 3
    #       /             \             /            \     
    #     __4___        __5___        __6___       __7__   
    #    /      \      /      \      /      \     /     \  
    #   15_    14_    13_    12_    11_    10_    9_    8_   flip: 13 -> 10, because f(k) = (8 + 15) - k = (2^3 + 2^4 - 1) - k = (2^3 * 3 - 1) - k, k = 13
    #  /   \  /   \  /   \  /   \  /   \  /   \  /  \  /  \
    # 16  17 18  19 20  21 22  23 24  25 26  27 28 29 30  31
    for i in range(len(ans) - 2, 0, -2):
      ans[i] = 2 ** i * 3 - 1 - ans[i]
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    14, 26, 42, 85,
  ]
  rslts = [solver.pathInZigZagTree(label) for label in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
