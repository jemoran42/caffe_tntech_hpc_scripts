import csv
import os

def convert_csv_to_arrays(filename, old_index, new_index):
    old_file = []
    new_file = []
 
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            old_file.append(row[old_index])
            new_file.append(row[new_index])
 
    return old_file, new_file
	
old_file,new_file = convert_csv_to_arrays('/path_to_dir/cars_annos.csv', 7, 8)

path = '/home/tntech.edu/yourusername/path_to_dir/car_ims'

for i in range(len(old_file)):
	for files in os.listdir(path):
		if old_file[i] in files:
			os.rename(os.path.join(path, old_file[i]), os.path.join(path, new_file[i]))
			print old_file[i] + ' to ' + new_file[i]
