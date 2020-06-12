itemlist = []
text = input("Gimme an item")
while (text != "stop"):
	itemlist.append(text)
	text = input("Gimme an item")

remove = input("What should I remove?")
for i in itemlist:
	if i == remove:
		itemlist.remove(i)
print(itemlist)
	