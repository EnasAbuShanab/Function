def sayHello():
  print("Hello")
  x=5
  x=x+1
  print(x)
sayHello()

print("\n")

def add(a,b):
  print (a+b)
add (12,451)

print("\n")

def add(x,y=5):
  """return x plus y, optional """
  return x + y
add(3,10)

print("\n")

def addtwo(a,b):
  added=a+b
  return added
x= addtwo(3,5)
print(x)

print("\n")

a=10
def someFunction():

  a=a+5
someFunction()
print(a)