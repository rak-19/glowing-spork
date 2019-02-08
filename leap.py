yearleap=int(input())
if((yearleap%400==0) or((yearleap%4 ==0)and(yearleap%100 !=0))):
 print("yes")
else:
  print("no")
