yearrk=int(input())
if((yearrk%400==0) or((yearrk%4 ==0)and(yearrk%100 !=0))):
 print("yes")
else:
  print("no")
