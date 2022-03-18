import argparse
import matplotlib.pyplot as plt
import os

def multiplot(languages, numbers, trials):
	for language in languages:
		x, y = [], []
		filename = f'{language}_{numbers}_{trials}'
		with open(filename) as file:
			for line in file:
				n, probability = parse(line)

				x.append(n)
				y.append(probability)

		_plot(x, y, language)

	_plot_graph('number', 'probability', f'{numbers}_{trials}', True)

# np.std(a, dtype=np.float64)
def create_analysis(language, numbers, trials, include_expected=False):
	x, y = [], []

	save_language=language
	if include_expected:
		language='expected'

	filename = f'{language}_{numbers}_{trials}'
	with open(filename) as file:
		for line in file:
			n, probability = parse(line)

			x.append(n)
			y.append(probability)
			# deviations.append(calculate_deviation(n, probability, expected))

	_plot(x, y, language)

	if include_expected:
		create_analysis(save_language, numbers, trials)
	else:
		_plot_graph('number', 'probability', f'{language}_{numbers}_{trials}', True)

def deviations(errors):
	return sum(errors) / len(errors)

# error : deviations.append(abs(expected - probability))
# average error for langauge trial : error summation / avg

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
def _plot(x, y, label):
	plt.plot(x, y, label=label)

def _plot_graph(x_axis, y_axis, title, save=False):
	plt.legend(loc='best')

	plt.xlabel(x_axis)
	plt.ylabel(y_axis)

	plt.title(title)

	if save:
		plt.savefig(f'graphs/{title}.png', bbox_inches='tight')

	plt.clf()

def parse(line):
	s = line.split(":")
	
	n = float(s[0].strip())
	probability = float(s[1].strip())

	return [n + 1, probability]

# Two Tailed Test
# Uniform Distribution
# Confidence Interval : 95

# Significance level 0.05


# mean = a + b / 2 = 4.5
# std = 9 / sqrt
def calculate_deviation(n, probability, expected):
	# print(n, probability, expected)
	deviation = abs(expected - probability)

	percent_err = deviation / probability

	return percent_err

	# return statistical_significance ** 2

def calculate_variance(deviations):

	# m = sum(deviations) / len(deviations)

	return sum(x ** 2 for x in deviations)

	# return m ** (1/2)

	# confidence_zscore = {90: 1.645, 95: 1.96, 98: 2.33, 99: 2.575}

	print(n, probability, expected)
	return 1

def parse_output_filenames():
	'''
	 Expecting to be within /outputs/
	'''
	ls = os.listdir()

	languages = set()
	options = set()
	for file in ls:
		if "_" in file:
			fileparts = file.split("_")
			
			language = fileparts[0]
			numbers = int(fileparts[1])
			trials = int(fileparts[2])

			option_tuple = (numbers, trials)

			languages.add(language)
			options.add(option_tuple)

	return (languages, options)

def plot_all_individual(include_expected=False):
	# ../outputs/
	os.chdir('../outputs/')
	languages, options = parse_output_filenames()

	for language in languages:
		for option in options:
			numbers = option[0]
			trials = option[1]
			create_analysis(language, numbers, trials, include_expected)

def plot_all_multi():
	# ../outputs/
	os.chdir('../outputs/')
	languages, options = parse_output_filenames()
	
	for option in options:
		numbers = option[0]
		trials = option[1]
		multiplot(languages, numbers, trials)

def plot_specific(language, number, trial):
	create_analysis(language, numbers, trials)

	# multiplot(languages, numbers, trials)

# plot_all_individual(True)
plot_all_multi()

# languages = get_languages()
# print(languages)

# options = get_options()
# print(options)

# py analysis.py --file ../outputs/go_10_1000000000
# if __name__ == '__main__':
# 	parser = argparse.ArgumentParser(description='argparse')
# 	parser._action_groups.pop()

# 	required = parser.add_argument_group('required arguments')
# 	required.add_argument('--file', type=argparse.FileType('r'), required=True)

# 	args = parser.parse_args()

# 	# print(dir(args.filename))

# 	analysis(args.file)