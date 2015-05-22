#! /usr/bin/python

class Employee:
	'Common base class for all employees'
	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def dispalyEmployee(self):
		print "Name : ", self.name, ", Salary : ", self.salary


emp1 = Employee("Beibei", 10000)
emp2 = Employee("Daxiong", 10000)

emp1.dispalyEmployee()
emp2.dispalyEmployee()
print "Total Employees %d" % Employee.empCount

emp1.age = 7 # Add an 'age' attribute.
emp1.age = 8 # Modify 'age' attribute.
print "Employee1's age : %d" % emp1.age
del emp1.age # Delete 'age' attribute.


