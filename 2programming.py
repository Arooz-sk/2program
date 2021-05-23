def validate(n,passw):
  SpecialSym =['$', '@', '#', '%','!']
  d = 0
  l = 0
  u = 0
  s = 0
  for char in passw:
    if (char.isdigit()):
      d += 1
  for char in passw:
    if (char.isupper()):
      u += 1 
  for char in passw:
    if (char.islower()):
      l += 1
  for char in passw:
    if (char in SpecialSym):
      s += 1 

  print('Password contains:')
  print('Special Character -',s)
  print('Digits -',d)
  print('Uppercase Alphabet -',u)
  print('Lowercase Alphabet -',l)
n = int(input())
passw  = input()
add  = minChar(n,passw)
validate(n,passw)
if(add == 0):
  print(add,'more characters should be added')
else:
  print('Strong Password, good to go!')