from typing import List

class Solution:
  def isSelfCrossing(self, x: List[int]) -> bool:
    """     N
            ^
            |
      W <--- ---> E
            |
            v
            S

    Self-Crossing Scenarios:

              Case 1                  Case 2                  Case 3               
                b                       b                       b                  
       +----------------+      +----------------+      +----------------+          
       |                |      |                |      |                |          
       |                |      |                |      |                |          
     c |                | a  c |                | a  c |                | a        
       |                |      |                |      |                |    f     
       +--------------->|      |                |      |                | <----+   
                d       |      |                ^ e    |                |      | e 
                               |                |      |                       |   
                               +----------------+      +-----------------------+   
                                        d                       d                  
    """
    a, b, c, d, e, f = [-1] * 6
    for z in x:
      f, e, d, c, b, a = e, d, c, b, a, z
      if d >= 0 and (c <= a) and (d >= b):
        return True
      if e >= 0 and (c > a) and (d == b) and (e >= c - a):
        return True
      if f >= 0 and (c > a) and (d > b) and (e >= c - a and e <= c) and (f >= d - b):
        return True
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0],
    [0,0],
    [0,0,0],
    [0,0,0,0],
    [1],
    [2,1,2],
    [2,1,5,6,2,3],
    [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3],
  ]
  rslts = [solver.isSelfCrossing(x) for x in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")