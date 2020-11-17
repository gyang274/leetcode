from typing import List
from itertools import accumulate
from functools import lru_cache

class Solution:
  @lru_cache(None)
  def recursive(self, i, j):
    score = 0
    if i < j:
      for k in range(i, j):
        L = self.prefix[k + 1] - self.prefix[i]
        R = self.prefix[j + 1] - self.prefix[k + 1]
        if L > R:
          score = max(score, R + self.recursive(k + 1, j))
        elif L < R:
          score = max(score, L + self.recursive(i, k))
        else:
          score = max(score, L + self.recursive(i, k), R + self.recursive(k + 1, j))
    return score
  def stoneGameV(self, stoneValue: List[int]) -> int:
    self.prefix = list(accumulate(stoneValue, initial=0))
    self.recursive.cache_clear()
    return self.recursive(0, len(stoneValue) - 1)

# from collections import defaultdict

# class Solution:
#   def stoneGameV(self, stoneValue: List[int]) -> int:
#     memo, n, prefix = defaultdict(lambda: 0), len(stoneValue), list(accumulate(stoneValue, initial=0))
#     for j in range(n):
#       for i in range(j - 1, -1, -1):
#         if i + 1 == j:
#           memo[(i, j)] = min(stoneValue[i:(j + 1)])
#         else:
#           for k in range(i, j):
#             L, R = prefix[k + 1] - prefix[i], prefix[j + 1] - prefix[k + 1]
#             if L <= R:
#               memo[(i, j)] = max(memo[(i, j)], prefix[k + 1] - prefix[i] + memo[(i, k)])
#             if R <= L:
#               memo[(i, j)] = max(memo[(i, j)], prefix[j + 1] - prefix[k + 1] + memo[(k + 1, j)])
#     return memo[(0, n - 1)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # 18
    [6,2,3,4,5,5],
    # 330
    [98,77,24,49,6,12,2,44,51,96],
    # 3163719
    [714981,672493,337882,360864,978610,831103,24792,497562,905131],
    # 172028529
    [956064,694292,49196,493294,865963,197259,335598,137835,453170,931714,242198,483056,856202,706346,797927,341019,54532,425143,605412,457444,75183,404645,564389,467033,374921,206984,840766,974212,782723,664108,474210,103246,952014,437659,687423,664444,717806,433320,431015,282111,101641,872381,159031,75843,612313,685379,320631,93905,142975,337146,676788,58873,589916,769288,680932,273313,350564,190419,980416,896215,780253,306896,433643,127543,481566,88968,699755,80911,558847,66321,475257,800162,757882,64719,152161,823547,447516,352647,568721,940521,965423,211779,947905,902589,653815,793026,817372,579181,393857,637632,645695,877571,285150,834400,543107,126361,922827,277302,331793,239340,226827,237277,763620,465066,925128,331068,715483,889489,296296,310163,236127,13841,924451,39863,880389,848987,167906,807468,72372,320095,747692,783755,12695,597256,965960,581080,522874,508710,987140,409482,763487,646782,724469,858581,185205,844252,232334,702737,749176,371175,124514,997312,992194,791731,933589,680596,492487,226751,452230,55615,881147,985619,868791,43421,520721,862777,399308,471777,728506,289412,530506,683593,237577,39100,566650,13418,142413,408557,184744,71550,723987,892123,913767,270951,225282,658277,819039,303825,770231,683521,672908,600117,590094,815122,606613,367486,58966,289457,545098,792270,73936,139583,371453,574540,685599,422383,320499,596546,812516,202880,583979,809739,790384,636168,68929,777428,946723,772750,849754,92985,897881,728375,975664,667664,464676,610209,462434,913271,11942,451710,865573,381767,72707,888982,694370,962186,197947,362664,615307,836244,461435,638583,948938,979372,950705,743992,614335,802785,330507,261749,210334,524924,298249,648008,414326,457743,626209,73076,760024,956323,184036,254921,254599,422956,934773,152498,317096,192955,212461,93692,160473,148377,556996,222652,380226,884143,597058,882482,986415,981536,556068,523574,925541,372098,696904,831359,834141,116113,19516,650976,916568,861144,437962,707126,619368,687011,137766,345282,664976,2466,308534,485962,121930,212750,603802,391435,980791,44837,575326,664684,292319,860075,126458,421786,436342,590078,869104,184818,315462,235878,745200,132537,298120,89202,435897,629368,25926,288960,314458,864044,529790,808570,87991,10047,49296,632469,578171,117479,64299,827209,138991,269771,494277,711190,750782,592251,157027,114549,144957,558169,180337,793779,314348,895311], 
  ]
  rslts = [solver.stoneGameV(stoneValue) for stoneValue in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
