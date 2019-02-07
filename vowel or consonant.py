rak=input()
vowel=("a","e","i","o","u")
if(rak>"a" and rak<"z" or rak>"A" and rak<"Z"):
  if rak in vowel:
    print("vowel")
  else:
    print("consonant")
else:
  print("invalid")
