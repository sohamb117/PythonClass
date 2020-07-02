import csv

## Opening files and context management

with open('file.txt','r+') as f:
	f_contents = f.read()
	print(f_contents)

## Opening CSV

with open('csvfile.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for element, number, avatar in csv_reader:
		print(element, number, avatar)file.open("file.txt", "r")