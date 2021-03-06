from calculator import Calculator
from shape import Shape
from bankAccount import BankAccount
from employee import Employee

print("------- TEST Calculator -------")
cal = Calculator()


print(cal.add("2","2"))
print(cal.multiply(2,10))
print(cal.subtract(100, 99))

print(cal.divide(10, 0))

print(cal.divide2(10, 2))

cal.printOperations()


print("------- TEST Shape -------")

x = 0
y = 5

shape = Shape(1, 2, "red")
shape1 = Shape(1, "two", "red")
shape2 = Shape(2, 1, 3)
shape3 = Shape("asdas", "asdas", "red")
shape4 = Shape(x, y, "red")

distance = shape.distance(shape2)
print(distance)

# Shape.printShape(s) # zle

shape.printShape()  # dobrze 
print(shape.printShape())
shape.distance(shape2)


print("------- TEST BankAccount -------")

ba = BankAccount(123456)
ba.printInfo()
ba.depositCash(130.0)

ba.depositCash(1)
ba.printInfo()

# ba.depositCash("123")

sto = 100.00
ba.withdrawtCash(sto)
ba.printInfo()

ba.withdrawtCash(100)
ba.printInfo()

ba.withdrawtCash(-10)
ba.printInfo()

print(ba.getCash())

print("------- TEST Employee -------")

e = Employee(1, "Alicja", "Baszak", 10)
e.printInfo()

e.raiseSalary(100)
e.printInfo()

e.raiseSalary(100)
e.printInfo()
