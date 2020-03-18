class Solution:
  def decodeString(self, s: str) -> str:
    stack, u = [], ""
    for x in s:
      if x == "[":
        stack.append(u)
        u = ""
      elif x == "]":
        v = stack.pop()
        while not v.isdigit():
          u = v + u
          v = stack.pop()
        stack[-1] += int(v) * u
        u = ""
      elif x.isdigit():
        if u.isdigit():
          u += x
        else:
          stack.append(u)
          u = x
      else:
        u += x
    stack.append(u)
    return "".join(stack)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "3[a]",
    "a2[b]",
    "a3[b]c",
    "3[a2[b]]",
    "3[a2[b]c]",
    "3[a2[b4[c]]]",
    "3[a2[b]]4[c]",
    "3[a]2[b4[F]c]",
    "3[z]2[2[y]pq4[2[jk]e1[f]]]ef",
  ]
  rslts = [solver.decodeString(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
