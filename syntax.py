import sys

varNames = []
varValues = []

def Raise(string):
  print(string)
  sys.exit()

def getInfo(syntax,line):
  code = syntax.split(" ")
  if code[0] == "display":
    if code[1] == "var":
      if code[2] in varNames:
        return f"print ('{varValues[varNames.index(code[2])]}')"
      else:
        Raise(f'ValueError: Line {line}: {code[2]} not found')
    elif code[1] == str:
      if type(code[2]) == "str" or str:
        code.pop(0)
        code.pop(0)
        displays = " ".join(code)
        return f"print('{displays}')"
      else:
        Raise(f'ValueError : Line {line}: {code[2]} not str')
    else:
       Raise(f'NameError : Line {line}:  {code[1]} not a valid type')
  elif code[0] == "create_var":
    if " " or r"\" in code[1]:
      Raise(f"VarError: Line {line}:  {code[1]} has a space. Variable names should not have spaces")
    else:
      varNames.append(code[1])
      code.pop(0)
      code.pop(0)
      value = " ".join(code)
      varValues.append(value)
  elif code[0] == "//":
    pass
  elif code[0] == "set_var":
    if code[1] in varNames:
      varName = code[1]
      code.pop(0)
      code.pop(0)
      value = " ".join(code)
      varValue[varNames.index(varName)] = value
    else:
      Raise(f"NameError: Line {line}: {code[1]} not defined")
  elif code[0] == "":
