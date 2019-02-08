prime=int(input())
prime<=1000
if prime>1:
 for i in range(2,prime):
  if (prime % i)==0:
      print("no")
      break
 else:
      print("yes")
else:
   print("no")     
