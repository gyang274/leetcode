from typing import List
from collections import defaultdict

class Solution:
  def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    d = defaultdict(lambda: 0)
    for cpdomain in cpdomains:
      count, domain = cpdomain.split(' ')
      count = int(count)
      domain = domain.split('.')
      d[domain[-1]] += count
      for i in range(len(domain) - 2, -1, -1):
        domain[i] += '.' + domain[i + 1]
        d[domain[i]] += count
    return [str(d[k]) + ' ' + k for k in d]
