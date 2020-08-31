class Solution:
  def defangIPaddr(self, address: str) -> str:
    return '[.]'.join(address.split('.'))

class Solution:
  def defangIPaddr(self, address: str) -> str:
    return address.replace('.','[.]')

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "127.0.0.1",
  ]
  rslts = [solver.defangIPaddr(address) for address in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
