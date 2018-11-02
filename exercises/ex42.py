# Animal is-a object (yes, sort confusing) look at the extra credit
class Animal(object):
	pass

## has-a
class Dog(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## has-a
class Cat(Animal):

	def __init__(self, name):
		## ??
		self.name = name

## is-a
class Person(object):

	def __init__(self, name):
		## is-a
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## has-a
class Employee(Person):

	def __init__(self, name, salary):
		## has-a hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## is-a
		self.salary = salary

## is-a
class Fish(object):
	pass

## has-a
class Salmon(Fish):
	pass

## has-a
class Halibut(Fish):
	pass


## rover is-a dog
rover = Dog("Rover")

## is-a
satan = Cat("Satan")

## is-a
mary.pet = satan

## is-a
frank.pet = satan

## is-a
frank = Employee("Frank", 120000)

## has-a
Frank.pet = rover

## has-a
flipper = Fish()

## has-a
crouse = Salmon()

## has-a
harry = Halibut()
