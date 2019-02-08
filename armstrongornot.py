rak=int(input())
tik=list(map(int,str(rak)))
tok=list(map(lambda x:x**3,tik))
if(sum(tok)==rak):
  print("yes")
else:
    print("no")
