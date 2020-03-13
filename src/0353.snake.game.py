from collections import deque

class SnakeGame:

  def __init__(self, width: int, height: int, food: List[List[int]]):
    """Initialize your data structure here.
      @param width - screen width
      @param height - screen height 
      @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
    """
    self.width = width
    self.height = height
    self.food = deque(food)
    self.snake = deque([(0, 0), ])
    self.direction = {
      'U': (-1,  0),
      'L': ( 0, -1),
      'R': ( 0,  1),
      'D': ( 1,  0),
    }

  def move(self, direction: str) -> int:
    """Moves the snake.
      @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
      @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
    """
    # move to (row, col)
    nr, nc = self.snake[-1][0] + self.direction[direction][0], self.snake[-1][1] + self.direction[direction][1]
    # move hit boundary?
    if not (0 <= nr < self.height and 0 <= nc < self.width):
      return -1
    # move hit snake body?
    snakeTail = self.snake.popleft()
    if (nr, nc) in self.snake:
      return -1
    self.snake.append((nr, nc))
    # move eat food?
    if self.food and [nr, nc] == self.food[0]:
      self.food.popleft()
      self.snake.appendleft(snakeTail)
    return len(self.snake) - 1
