def troca(s):

  if len(s) <= 1: return s 
  else: 
    first = s[0]
    last = s[-1]
    new = last + s[1:-1] + first
    return new

print(troca("Chocolate"))