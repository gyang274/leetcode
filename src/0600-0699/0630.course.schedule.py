from typing import List

import heapq

class Solution:
  def scheduleCourse(self, courses: List[List[int]]) -> int:
    """O(NlogN)
    """
    # it is always profitable to take the course with a smaller end day prior to a course with a larger end day
    courses.sort(key=lambda x: (x[1], x[0]))
    T, queue = 0, []
    for course in courses:
      if T + course[0] <= course[1]:
        # take this course
        T += course[0]
        heapq.heappush(queue, -course[0])
      elif queue and queue[0] + course[0] < 0:
        # take this course by replacing the most time consuming course C taken
        # must ok because course C can be taken and has an end day earlier than this course.
        T += queue[0] + course[0]
        heapq.heappop(queue)
        heapq.heappush(queue, -course[0])
    return len(queue)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,2],[2,3]],
    [[5,5],[4,6],[2,6]],
  ]
  rslts = [solver.scheduleCourse(courses) for courses in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")