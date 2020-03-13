from collections import defaultdict

class Logger:

  def __init__(self):
    """Initialize your data structure here.
    """
    self.messages = defaultdict(lambda: 0)

  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    """Returns true if the message should be printed in the given timestamp, otherwise returns false.
      If this method returns false, the message will not be printed. The timestamp is in seconds granularity.
    """
    if message in self.messages and timestamp - self.messages[message] < 10:
      return False
    else:
      self.messages[message] = timestamp
      return True

# TODO: keep more than necessary message, should keep all in last 10s will be enough..