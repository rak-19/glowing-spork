rak=raw_input()
vowel=("a","e","i","o","u")
if(rak>="a" and rak<="z"):
  if rak in vowel:
    print("vowel")
  else:
    print("consonant")
else:
  print("invalid")
