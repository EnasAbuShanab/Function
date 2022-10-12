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
print(add(3,10),"\n")
print("\n")

def addtwo(a,b):
  added=a+b
  return added
x= addtwo(3,5)
print(x)

print("\n")

a=10
def someFunction():
  global a
  a=a+5
someFunction()
print(a)

print("\n")

se={"saif":100, "Muh":200}
def updateseByRef(se):
  newse={"nour":100,"toqa":220}
  se.update(newse)
  print(se,"\n")
updateseByRef(se)
print("inside the function update by reference",se)

print("\n")

se={"saif":100, "Muh":200}
def updateseByVal(se):
  se={"nour":100,"toqa":220}
  se.update(se)
  print(se,"\n")
updateseByVal(se)
print("inside the function update by reference",se)

print("\n")

se=5
def updateseByVal(se):
  se=se+10
  print(se,"\n")

updateseByVal(se)
print(se)

print("\n")

class employee:
  'Common base class for all employees'
  empCount=0
  def __init__ (self,name, salary):
    self.name= name
    self.salary=salary
    employee.empCount +=1
  
  def displayCount(self):
    print("total emp."%employee.empCount)
#unusable functions
  def displayCount(self):
    print("Name: ",self.name,",Salary: ",self.salary)

emp1=employee("ahmed",100)
emp2=employee("zaid",300)
print(emp1.name)
print(emp1.salary)

  #def displayCount (self):
    #print ()
    