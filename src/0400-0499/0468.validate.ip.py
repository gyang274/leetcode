class Solution:
  def __init__(self):
    self.hexdigits = set('0123456789abcdefABCDEF')
  def isIPv4(self, ip4):
    """Q0093.
    """
    for num in ip4:
      if not (num.isdigit() and int(num) <= 255 and (len(num) == 1 or not num[0] == "0")):
        return False
    return True
  def isIPv6(self, ip6):
    for num in ip6:
      if not (0 < len(num) <= 4 and all([x in self.hexdigits for x in num])):
        return False
    return True
  def validIPAddress(self, IP: str) -> str:
    ip4 = IP.split(".")
    if len(ip4) == 4 and self.isIPv4(ip4):
      return "IPv4"
    ip6 = IP.split(":")
    if len(ip6) == 8 and self.isIPv6(ip6):
      return "IPv6"
    return "Neither"

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "172.16.254.1",
    "256.256.256.256",
    "2001:0db8:85a3::0:8A2E:0370:7334",
    "2001:0db8:85a3:0:0:8A2E:0370:7334",
    "1081:db8:85a3:01:-0:8A2E:0370:7334",
    "2001:0db8:85a3:0000:0000:8A2E:0370:7334",
    "2001:0db8:85a3:0000:0000:8A2E:0070:7334",
    "2001:0db8:85a3:0000:0000:8A2E:0070:73z4",
    "02001:0db8:85a3:0000:0000:8A2E:0070:7334",
  ]
  rslts = [solver.validIPAddress(IP) for IP in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")