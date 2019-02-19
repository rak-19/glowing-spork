a=int(input("operand1:"))
b=int(input("operand2:"))
print("1.ADD")
print("2.SUB")
print("3.MUL")
print("4.DIV")
operation=float(input("enter 1 or 2 or 3 or 4 :"))
operation=round(operation)
if(operation==1): 
  c=a+b
  print(c)
elif(operation==2):
  c=a-b
  print(c)
elif(operation==3): 
  c=a*b
  print(c)
elif(operation==4):
  if b==0:
    print("infinity")
  else:
    c=a/b
else:
  print("invalid")

