# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
  # def move(self):
  #   """
  #   Returns true if the cell in front is open and robot moves into the cell.
  #   Returns false if the cell in front is blocked and robot stays in the current cell.
  #   :rtype bool
  #   """

  # def turnLeft(self):
  #   """Robot will stay in the same cell after calling turnLeft/turnRight.
  #   Each turn will be 90 degrees.
  #   :rtype void
  #   """

  # def turnRight(self):
  #   """Robot will stay in the same cell after calling turnLeft/turnRight.
  #   Each turn will be 90 degrees.
  #   :rtype void
  #   """

  # def clean(self):
  #   """Clean the current cell.
  #   :rtype void
  #   """

class Solution:

  def _stepback(self):
    self.robot.turnRight()
    self.robot.turnRight()
    self.robot.move()
    self.robot.turnRight()
    self.robot.turnRight()

  def backtrack(self, x, y, d):
    self.robot.clean()
    self.visited.add((x, y))
    for dd in range(4):
      k = (d + dd) % 4
      i, j = x + self.direction[k][0], y + self.direction[k][1]
      if (i, j) not in self.visited and self.robot.move():
        self.backtrack(i, j, k)
      self.robot.turnRight()
    self._stepback()

  def cleanRoom(self, robot: "Robot") -> None:
    # maze solving algorith, right hand rule, https://en.wikipedia.org/wiki/Maze_solving_algorithm
    self.robot= robot
    self.visited = set([])
    self.direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    self.backtrack(0, 0, 0)
