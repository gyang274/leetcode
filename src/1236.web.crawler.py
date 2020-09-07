# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser:
#   def getUrls(self, url: str) -> List[str]:

class Solution:
  def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
    hostname, urls = startUrl.split('/')[2], set([startUrl])
    queue = [startUrl]
    for u in queue:
      for v in htmlParser.getUrls(u):
        if v not in urls and v.split('/')[2] == hostname:
            queue.append(v)
            urls.add(v)
    return urls
