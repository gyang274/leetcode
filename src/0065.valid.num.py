class Solution:
  def isNumber(self, s: str) -> bool:
    """DFA: deterministic finite automaton
    """
    if not s: 
      return False
    # define the state
    state = [
      # at state 0
      # if blank, back to 0, next can be blank, or sign, or digit,
      # if sign, go to state 1, next must be digit
      # if digit, go to state 2, next can be digit, or dot, or exponent
      {'blank': 0, 'sign': 1, 'digit': 2, 'dot': 3},
      # state1: '[ ](+-)'
      # [] means optional, () mean must one from set, {} means must have the set of not
      {'digit': 2, 'dot': 3},
      # state2: '[ (+-)]X', ok as ende
      {'digit': 2, 'dot': 4, 'exp': 5, 'blank': 8},
      # state3: '[ (+-)].'
      {'digit': 4},
      # state4: '[ (+-)]X.', ok as ende
      {'digit': 4, 'exp': 5, 'blank': 8},
      # state5: '[ (+-){X.}]Xe'
      {'digit': 7, 'sign': 6},
      # state6: '[ (+-){X.}]Xe(+-)'
      {'digit': 7},
      # state7: '[ (+-){X.}]Xe[(+-)]X', ok as ende
      {'digit': 7, 'blank': 8},
      # state7: '[ (+-){X.}{Xe[(+-)]}]X ', ok as ende
      {'blank': 8}
    ]
    cs = 0
    for x in s:
      # print(f"{s=}, {x=}, {state[cs]=}")
      # determin current character key
      if x == ' ':
        k = 'blank'
      elif x in ('+', '-'):
        k = 'sign'
      elif x >= '0' and x <= '9':
        k = 'digit'
      elif x == '.':
        k = 'dot'
      elif x == 'e':
        k = 'exp'
      else:
        return False
      # print(f"{s=}, {x=}, {state[cs]=}, {k=}")
      # determine whether key is appropriate in current state
      if k in state[cs]:
        # determine next state
        cs = state[cs][k]
      else:
        return False
    # determine ende state is ok or not
    if cs not in [2, 4, 7, 8]:
      return False
    return True


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    " ",
    "+",
    " +",
    " -",
    " +0",
    " -00",
    " -01",
    " .",
    " .1",
    " 0.",
    " .e1",
    " 1.e1",
    "0",
    " 0.1 ",
    "abc",
    "1 a",
    "2e10",
    " -90e3   ",
    " 1e",
    "e3",
    " 6e-1",
    " 99e2.5 ",
    "53.5e93",
    " --6 ",
    "-+3",
    "95a54e53",
  ]
  rslts = [solver.isNumber(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")