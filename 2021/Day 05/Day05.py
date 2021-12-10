from collections import Counter

def process_line(line):
	line = line.rstrip().replace(',',' ').replace('->', '').split()
	line = [int(x) for x in line]
	line = [(line[0],line[1]),(line[2],line[3])]
	return line

with open('input.txt') as file:
	lines = file.readlines()
	lines = [process_line(line) for line in lines]

all_points = []

def get_slope(p):
	try:
		slope = int((p[1][1]-p[0][1])/(p[1][0]-p[0][0]))
	except ZeroDivisionError:
		slope = None
	return slope

def add_point(px, py):
	global all_points
	all_points.append((px, py))

def walk_line(line, diagonals = False):
	line = sorted(line)
	slope = get_slope(line)
	match slope:
		case 0:
			for x in range(line[0][0], line[1][0] + 1):
				add_point(x, line [0][1])
		case None:
			for y in range(line[0][1], line [1][1] + 1):
				add_point(line[0][0], y)
		case _ if diagonals:
			for idx, x in enumerate(range(line[0][0], line [1][0] + 1)):
				add_point(x, line[0][1] + (slope * idx))

def count_overlaps():
	cnt = Counter(all_points)
	return sum(v > 1 for v in cnt.values())

def puzzle1():
	global all_points
	all_points = []
	
	for line in lines:
		walk_line(line)
	
	solution = count_overlaps()
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	global all_points
	all_points = []
	
	for line in lines:
		walk_line(line, True)
	
	solution = count_overlaps()

	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()