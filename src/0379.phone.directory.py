class PhoneDirectory:
  def __init__(self, maxNumbers: int):
    """Initialize your data structure here
      @param maxNumbers - The maximum numbers that can be stored in the phone directory.
    """
    # don't store all available number into hashset, since maxNumber might extremely large.
    # instead store maxUsed, and all recycled.
    self.maxNumbers = maxNumbers
    self.nextNumber = 0
    self.recycled = set([])

  def get(self) -> int:
    """Provide a number which is not assigned to anyone.
      @return - Return an available number. Return -1 if none is available.
    """
    if self.recycled:
      return self.recycled.pop()
    elif self.nextNumber < self.maxNumbers:
      x = self.nextNumber
      self.nextNumber += 1
      return x
    else:
      return -1 
    
  def check(self, number: int) -> bool:
    """Check if a number is available or not.
    """
    return number in self.recycled or self.nextNumber <= number < self.maxNumbers
    
  def release(self, number: int) -> None:
    """Recycle or release a number.
    """
    # only release unavailable number to recycled..
    if number >= 0 and not self.check(number):
      if number == self.nextNumber - 1:
        self.nextNumber -= 1
        # while max(self.recycled) == self.nextNumber - 1:
        #   self.recycled.remove(max(self.recycled))
        #   self.nextNumber -= 1
      else:
        self.recycled.add(number)