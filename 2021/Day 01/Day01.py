with open('input.txt') as file:
	lines = file.readlines()
	lines = [int(line.rstrip()) for line in lines]

def puzzle1():
	count = 0
	for i in range(len(lines) - 1):
		a = lines[i+1]
		b = lines[i]
		if a > b:
			count += 1
	print(f'Puzzle 1 Count: {count}')

def puzzle2():
	count = 0
	for i in range(len(lines) - 3):
		a = sum(lines[i+1:i+4])
		b = sum(lines[i:i+3])
		if a > b:
			count += 1
	print(f'Puzzle 2 Count: {count}')

puzzle1()
puzzle2()