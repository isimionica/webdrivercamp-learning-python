#!/usr/bin/python3
if __name__=="__main__":
  
  
  a = 4 #use this variable as a first argument to call a function 
  b = 2 #use this variable as a second argument to call a function
  
  def add (a,b):
    return a+b
  def sub (a,b):
    return a-b
  def multi (a,b):
    return a*b
  def div (a,b):
    return a/b

  c = add(a, b)
  print(c)
  d = sub(a, b)
  print(d)
  e= multi(a, b)
  print (e)
  f = div(a, b)
  print (f)



  
