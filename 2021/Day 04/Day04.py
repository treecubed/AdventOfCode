import copy

def process_line(line):
	line = [int(x) for x in line.rstrip().replace(',',' ').split()]
	return line

with open('input.txt') as file:
	lines = file.readlines()
	lines = [process_line(line) for line in lines]

class BingoCard(object):
	class ImproperSizeError(Exception):
		pass

	numbers = []
	marks_by_row = []
	marks_by_col = []
	empty_marks = [
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0]
	]

	def __init__(self, numbers):
		self.set_numbers(numbers)
		self.clear_marks()

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

	def mark_and_check(self, num):
		if self.mark_number(num):
			return self.check_board()
		return False

	def mark_number(self, num):
		for i in range(5):
			for j in range(5):
				if self.numbers[i][j] == num:
					# print(f'Marking number: {num} index: [{i}][{j}]')
					self.marks_by_row[i][j] = 1
					self.marks_by_col[j][i] = 1
					return True
		return False

	def clear_marks(self):
		self.marks_by_row = copy.deepcopy(self.empty_marks)
		self.marks_by_col = copy.deepcopy(self.empty_marks)

	def check_board(self):
		for i in range(5):
			if (
					not self.marks_by_row[i].count(0) or
					not self.marks_by_col[i].count(0)
				):
				return True
		return False

	def calc_score(self, num):
		score = 0
		for i in range(5):
			for j in range(5):
				if self.marks_by_row[i][j] == 0:
					score += self.numbers[i][j]
		score *= num
		return score

	# def __str__(self):
	# 	ret_str = ''
	# 	for row in self.numbers:
	# 		row_str = ','.join([str(x) for x in row])
	# 		ret_str += row_str + '\n'
	# 	return ret_str

	def __str__(self):
		ret_str = ''
		for i in range(5):
			for j in range(5):
				num_str = f'({self.marks_by_row[i][j]}){self.numbers[i][j]}, '
				ret_str += num_str
			if i != 4: ret_str += '\n'
		return ret_str

	def __repr__(self):
		return f'BingoCard({str(self.numbers)})'

call_numbers = []
board_numbers = []

def process_lines():
	global call_numbers, board_numbers
	call_numbers = lines[0]
	board_numbers = []
	numbers = []
	for row in lines[1:]:
		if row:
			numbers.append(row)
		elif len(numbers) == 5:
			board_numbers.append(numbers)
			numbers = []

def puzzle1():
	bingo_cards = []
	solution = -1
	for numbers in board_numbers:
		bingo_cards.append(BingoCard(numbers))

	for num in call_numbers:
		# print(f'Calling number: {num}')
		for card in bingo_cards:
			if card.mark_and_check(num):
				solution = card.calc_score(num)
				print(f'Last num was: {num}')
				print(f'Card num was: {bingo_cards.index(card)}')
				print('Card was:')
				print(card)
				break
		if solution != -1:
			break

	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	bingo_cards = []
	solution = -1

	for numbers in board_numbers:
		bingo_cards.append(BingoCard(numbers))

	for num in call_numbers:
		# print(f'Calling number: {num}')
		if len(bingo_cards) > 1:
			bingo_cards = [card for card in bingo_cards if not card.mark_and_check(num)]
		elif bingo_cards[0].mark_and_check(num):
			solution = bingo_cards[0].calc_score(num)
			print(f'Last num was: {num}')
			print(f'Card num was: {bingo_cards.index(bingo_cards[0])}')
			print('Card was:')
			print(bingo_cards[0])
			break
		if solution != -1:
			break

	print(f'Puzzle 2 solution: {solution}')

process_lines()
puzzle1()
puzzle2()
