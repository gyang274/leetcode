class Solution:
  def ip2int(self, ip):
    x = 0
    for s in ip.split('.'):
      x <<= 8
      x += int(s)
    return x
  def int2ip(self, x):
    # ip = ''
    # for _ in range(4):
    #   ip = str(x % 256) + ip
    #   x >>= 8
    # return ip
    return '.'.join(str((x >> i) % 256) for i in (24, 16, 8, 0))
  def ipToCIDR(self, ip, n):
    x = self.ip2int(ip)
    ans = []
    while n:
      mask = max(33 - (x & -x).bit_length(), 33 - n.bit_length())
      ans.append(self.int2ip(x) + '/' + str(mask))
      x += 1 << (32 - mask)
      n -= 1 << (32 - mask)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("255.0.0.5", 12),
    ("255.0.0.255", 256),
    ("255.0.0.255", 257),
  ]
  rslts = [solver.ipToCIDR(ip, n) for ip, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
