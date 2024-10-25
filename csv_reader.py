import	csv
import	sys

def	get_people_from_csv():
	if len(sys.argv) != 2:
		sys.exit("Usage: python your_script.py <path_to_csv>")
	csv_file_path = sys.argv[1]
	people = []

	with open(csv_file_path, mode='r') as file:
		csv_reader = csv.DictReader(file)
		for row in csv_reader:
			people.append(row)
	return people
