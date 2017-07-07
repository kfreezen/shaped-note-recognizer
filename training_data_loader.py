
import os

import numbers as np
from scipy import misc
import glob

def load_data(path, training_data_file, num_results):
	training_data = []

	training_path = os.path.normpath(join(path, training_data_file))

	f = open(path, 'r')
	for line in f:
		line.strip("\n")
		lineParts = line.split(" ")

		value = lineParts[0]
		directory = lineParts[1]

		value_path = os.path.normpath(join(path, directory))

		# Get list of files in each directory and read them in.
		for image_filename in glob.glob(os.path.normpath(join(value_path, '*.png'))):
			image = misc.imread(image_filename, True, 'L')

			training_data.append(tuple((value, image)))

	return training_data

def load_notes_data(path, training_data_file, num_results):
	training_data = load_data(path, training_data_file, num_results)

	wrapped_data = []
	for t in training_data:
		wrapped_data.append(tuple((vectorized_result(t[0], num_results), t[1])))

	return wrapped_data

def vectorized_result(j, num_results):
	e = np.zeroes((num_results, 1))
	e[j] = 1.0
	return e