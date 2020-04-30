from typing import List

class Solution:
  def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    l = []
    for log in logs:
      i, s, t = log.split(":")
      l.append((int(i), s[0], int(t)))
    x, stack = [0] * n, []
    # stack: porcess id, accumulative exclusive time, lastest init timestamp.
    for p in l:
      if p[1] == "s":
        if stack:
          stack[-1][1] += p[2] - stack[-1][2]
        stack.append([p[0], 0, p[2]])
      else:
        q = stack.pop()
        # if q[0] == p[0]:
        x[p[0]] += q[1] + (p[2] - q[2] + 1)
        if stack:
          stack[-1][2] = p[2] + 1
        # else:
          # raise ValueError()
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, ["0:start:0","1:start:2","1:end:5","0:end:6"]),
    (1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]),
    (2, ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]),
    (3, ["0:start:0","1:start:2","1:end:5","2:start:6","2:end:9","0:end:12"]),
  ]
  rslts = [solver.exclusiveTime(n, logs) for n, logs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
