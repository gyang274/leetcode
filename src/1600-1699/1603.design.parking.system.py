class ParkingSystem:

  def __init__(self, big: int, medium: int, small: int):
    self.x = [-1, big, medium, small]

  def addCar(self, carType: int) -> bool:
    self.x[carType] -= 1
    return self.x[carType] >= 0
