def process_point(point):
	point = point.split(',')
	point = (int(point[0]),int(point[1]))
	return point

def process_fold(fold):
	fold = fold.split()
	fold = fold[2].split('=')
	fold[1] = int(fold[1])
	return fold

with open('input.txt') as file:
	data = file.read().rstrip()
	data = data.split('\n\n')
	folds = data[1].split('\n')
	data = data[0].split('\n')
	data = [process_point(point) for point in data]
	folds = [process_fold(fold) for fold in folds]

def do_fold(sheet, fold):
	i =  0 if fold[0] == 'x' else 1
	f = fold[1]
	new_sheet = set()
	for point in sheet:
		point = list(point)
		if point[i] > f:
			point[i] = f - (point[i] - f)
		point = tuple(point)
		new_sheet.add(point)
	return new_sheet

def str_replace(string, index, char):
	return string[:index] + char + string[index + 1:]

def display(sheet):
	width = 0
	height = 0
	for point in sheet:
		if point[0] > width: width = point[0]
		if point[1] > height: height = point[1]
	width += 1
	height += 1
	grid = ['.' * width for y in range(height)]
	for point in sheet:
		grid[point[1]] = str_replace(grid[point[1]], point[0], '#')
	disp = '\n'.join(grid)
	print(disp)

def puzzle1():
	sheet = set(data)
	
	sheet = do_fold(sheet, folds[0])
	
	solution = len(sheet)
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	sheet = set(data)
	for fold in folds:
		sheet = do_fold(sheet, fold)

	print(f'Puzzle 2 solution:')
	display(sheet)

puzzle1()
puzzle2()