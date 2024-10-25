# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                  ____   ____       ____     ___                 #
#                 / ___| / ___|     | ___|   / _ \                #
#                | |     \___ \     |___ \  | | | |               #
#                | |___   ___) |     ___) | | |_| |               #
#                 \____| |____/     |____/   \___/                #
#                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import	csv

def	get_people_from_csv(csv_file_path):
	people = []

	with open(csv_file_path, mode='r') as file:
		csv_reader = csv.DictReader(file)
		for row in csv_reader:
			people.append(row)
	return people
