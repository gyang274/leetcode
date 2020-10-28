class BrowserHistory:

  def __init__(self, homepage: str):
    self.q = [homepage]
    self.i = 0

  def visit(self, url: str) -> None:
    self.q = self.q[:(self.i + 1)] + [url]
    self.i = len(self.q) - 1

  def back(self, steps: int) -> str:
    self.i = max(0, self.i - steps)
    return self.q[self.i]

  def forward(self, steps: int) -> str:
    self.i = min(self.i + steps, len(self.q) - 1)
    return self.q[self.i]
