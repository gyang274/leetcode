class Solution:
  def reformatDate(self, date: str) -> str:
    m = {
      "Jan": '01',
      "Feb": '02',
      "Mar": '03',
      "Apr": '04',
      "May": '05',
      "Jun": '06',
      "Jul": '07',
      "Aug": '08',
      "Sep": '09',
      "Oct": '10',
      "Nov": '11',
      "Dec": '12',
    }
    return date[-4:] + '-' + m[date[-8:-5]] + '-' + ('0' if len(date) == 12 else '') + date[:-11]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "2th Jul 1985",
    "17th Oct 2023",
  ]
  rslts = [solver.reformatDate(date) for date in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
