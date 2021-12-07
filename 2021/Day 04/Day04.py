def process_line(line):
	line = line.rstrip().split()
	return line

with open('input.txt') as file:
	lines = file.readlines()
	lines = [process_line(line) for line in lines]

class BingoCard:
	class ImproperSizeError(Exception):
		pass

	numbers = []
	marks = [
		[0,0,0,0,0],
		[0,0,0,0,0],
		[0,0,0,0,0],
		[0,0,0,0,0],
		[0,0,0,0,0]
	]

	def __init__(self, numbers):
		self.set_numbers(numbers)

	def set_numbers(self, numbers):
		is_valid = False
		if len(numbers) == 5:
			is_valid = True
			for row in numbers:
				if len(row) != 5:
					is_valid = False
		if not is_valid:
			raise self.ImproperSizeError('Numbers not correct size (5x5)')
		self.numbers = numbers

	def __str__(self):
		ret_str = ''
		for row in self.numbers:
			row_str = ','.join([str(x) for x in row])
			ret_str += row_str + '\n'
		return ret_str

	def __repr__(self):
		return f'BingoCard({str(self.numbers)})'


def puzzle1():



	solution = 0

	print(f'Puzzle 1 solution: {solution}')

def puzzle2():

	

	solution = 0

	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()