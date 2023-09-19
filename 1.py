import csv

def cardinality_items( filename ):
	with open(filename, 'r') as csv_file:
		csv_reader = csv.reader(csv_file)

		list = set()

		for line in csv_reader:
			for str in line:
				list.add(str)


		return len(list)





print(cardinality_items('basket_data.csv'))