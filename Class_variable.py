class Car:
	num_cars_made = 0
	num_doors = 4
	
	def __init__(self):
		# Change num_doors to a class variable!
		self.num_wheels = 4
		self.color = "boring gray"
		Car.num_cars_made += 1

################
# Every time you see num_cars_made
# from this point on, change it to
# num_doors and see what happens!
c1 = Car()
print c1.color

c2 = Car()
c2.color = "red"
print c2.color

print "#####"

print c1.num_doors

c1.num_doors = 10

print c1.num_doors
print c2.num_doors
print Car.num_doors
