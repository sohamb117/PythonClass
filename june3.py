shopping_list = ["Ice cream", "Cookies", "Pasta", "Corn","Potatoes", "Brownies"]
def add(item):
	shopping_list.append(item)
def remove(item):
	shopping_list.remove(item)
command = input("Add or remove?")
if command == "Add":
	product = input("What product?")
	add(product)
elif command == "Remove":
	product = input("What product?")
	remove(item)