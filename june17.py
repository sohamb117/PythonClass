import math
def sequence(start, difference):
	for x in range(start, 10001, difference):
		print(x)

start = int(input("Start:"))
difference = int(input("Difference:"))
sequence(start, difference)

def fibonacci(number):
	if number == 0:
		return(0)
	elif number == 1:
		return(1)
	else:
		return(fibonacci(number-1)+fibonacci(number-2))

print(fibonacci(24))

class circle:
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		return(self.radius * self.radius * math.pi)
	def circumference(self):
		return(self.radius*2*math.pi)

x = circle(10)
print(x.area())
print(x.radius)
print(x.circumference())

y = circle(13)
print(y.area())
print(y.radius)
print(y.circumference())

class rectprism:
	def __init__(self, dim1, dim2, dim3):
		self.width = dim1
		self.height = dim2
		self.depth = dim3
	def volume(self):
		return(self.width * self.height * self.depth)
	def surface_area(self):
		return(2*self.width*self.height + 2*self.width*self.depth + 2*self.height*self.depth)
	def edges(self):
		return(4*self.height + 4*self.width + 4*self.depth)

a = rectprism(10,10,10)
print(a.volume())
print(a.edges())
print(a.surface_area())