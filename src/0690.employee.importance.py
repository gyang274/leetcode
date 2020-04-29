"""Definition for Employee.
class Employee:
  def __init__(self, id: int, importance: int, subordinates: List[int]):
    self.id = id
    self.importance = importance
    self.subordinates = subordinates
"""

class Solution:
  def recursive(self, id):
    employee = self.d[id]
    score = employee.importance
    for subordinate in employee.subordinates:
      score += self.recursive(subordinate)
    return score
  def getImportance(self, employees: List['Employee'], id: int) -> int:
    self.d = {}
    for employee in employees:
      self.d[employee.id] = employee
    return self.recursive(id)
   