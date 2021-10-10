import argparse
import matplotlib.pyplot as plt
import os

languages = ['go', 'java', 'javascript', 'python']

def multiplot(numbers, trials):
	os.chdir('../outputs/')

	# for language in trials:
	# 	language, numbers, trials = parse_filename(language)
	expected = 1 / numbers

	for language in languages:
		x = []
		y = []
		with open(f'{language}_{numbers}_{trials}') as file:
			for line in file:
				n, probability = parse(line)

				x.append(n)
				y.append(abs(expected - probability))

		# deviations(y)	
		plt.plot(x, y, label=language)

		# deviations(y)

	plt.xlabel('value')
	plt.ylabel('error')
	plt.legend(loc='best')

	title = f'{numbers} range : {trials} iterations'
	plt.title(title)

	plt.show()
	# plt.savefig(f'{title}.png', bbox_inches='tight')

# np.std(a, dtype=np.float64)
def analysis(file):
	language, numbers, trials = parse_filename(file.name)
	expected = 1 / numbers

	x = []
	y = []
	for line in file:
		n, probability = parse(line)

		x.append(n)
		y.append(abs(expected - probability))
		# deviations.append(calculate_deviation(n, probability, expected))

	plot(x, deviations, 'value', 'error', f'{language}_{numbers}_{trials}')
	# individual plots, multi plot across languages

	# read all files in directory

def deviations(errors):
	return sum(errors) / len(errors)

# error : deviations.append(abs(expected - probability))
# average error for langauge trial : error summation / avg

def plot(x, y, x_name, y_name, title):
	plt.plot(x, y)

	plt.xlabel(x_name)
	plt.ylabel(y_name)

	plt.title(title)

	# plt.show()

	plt.savefig(f'{title}.png', bbox_inches='tight')

def parse_filename(filename):
	filename = filename.split("/")[-1]

	s = filename.split("_")
	language = s[0]
	numbers = int(s[1])
	trials = int(s[2])

	return [language, numbers, trials]

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

multiplot(10, 1000000)

# py analysis.py --file ../outputs/go_10_1000000000
# if __name__ == '__main__':
# 	parser = argparse.ArgumentParser(description='argparse')
# 	parser._action_groups.pop()

# 	required = parser.add_argument_group('required arguments')
# 	required.add_argument('--file', type=argparse.FileType('r'), required=True)

# 	args = parser.parse_args()

# 	# print(dir(args.filename))

# 	analysis(args.file)