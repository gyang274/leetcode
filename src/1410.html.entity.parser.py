class Solution:
  def entityParser(self, text: str) -> str:
    text = text.replace('&gt;', '>')
    text = text.replace('&lt;', '<')
    text = text.replace('&quot;', '"')
    text = text.replace('&apos;', "'")
    text = text.replace('&frasl;', '/')
    # process &amp; at last
    text = text.replace('&amp;', '&')
    return text

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "I quote: &quot;...&quot;",
    "stay home! practice on leetcode :)",
    "x &gt; y &amp;&amp; x &lt; y is always false",
    "&amp; is an HTML entity but &ambassador; is not.",
  ]
  rslts = [solver.entityParser(text) for text in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
