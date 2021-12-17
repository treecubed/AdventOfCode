from colorama import Fore
from colorama import Style
import random
from math import prod

def process_line(line):
	line = list(line.rstrip())
	line = [int(x) for x in line]
	return line

with open('input.txt') as file:
	lines = file.readlines()
	data = [process_line(line) for line in lines]

styles = {}

def random_color():
	colors = [
		Fore.LIGHTBLACK_EX,
		Fore.WHITE,
		Fore.LIGHTWHITE_EX,
		Fore.YELLOW,
		Fore.LIGHTYELLOW_EX,
		Fore.BLUE,
		Fore.LIGHTBLUE_EX,
		Fore.CYAN,
		Fore.LIGHTCYAN_EX,
		Fore.GREEN,
		Fore.LIGHTGREEN_EX,
		Fore.MAGENTA,
		Fore.LIGHTMAGENTA_EX,
		Fore.RED,
		Fore.LIGHTRED_EX
	]
	return random.choice(colors)

def get_low_points():
	lps = []
	for i in range(len(data)):
		for j in range(len(data[i])):
			low = True
			if i > 0:
				if data[i][j] >= data[i-1][j]:
					low = False
			if i < len(data) - 1:
				if data[i][j] >= data[i+1][j]:
					low = False
			if j > 0:
				if data[i][j] >= data[i][j-1]:
					low = False
			if j < len(data[i]) - 1:
				if data[i][j] >= data[i][j+1]:
					low = False
			if low:
				lps.append((i,j))
				styles[(i,j)] = random_color() + Style.BRIGHT
			if data[i][j] == 9:
				styles[(i,j)] = Fore.BLACK
	return lps

def get_basins():
	ret = [[idx, [p]] for idx, p in enumerate(low_points)]
	crawl_list = [(idx, p[0], p[1]) for idx, p in enumerate(low_points)]
	def check(b, x, y):
		if data[x][y] != 9:
			if (b, x, y) not in crawl_list:
				ret[b][1].append((x, y))
				crawl_list.append((b, x, y))
				styles[(x,y)] = styles[ret[b][1][0]]
	for basin, i, j in crawl_list:
		if i > 0:
			check(basin, i-1, j)
		if i < len(data) - 1:
			check(basin, i+1, j)
		if j > 0:
			check(basin, i, j-1)
		if j < len(data[i]) - 1:
			check(basin, i, j+1)
	return ret

def display():
	disp = ''
	for i in range(len(data)):
		for j in range(len(data[i])):
			if (i,j) in styles:
				disp += styles[(i,j)]
			disp += str(data[i][j]) + Style.RESET_ALL
		disp += '\n'
	print(disp)

def puzzle1():
	
	solution = sum([data[i][j] for i, j in low_points]) + len(low_points)
	
	print(f'Puzzle 1 solution: {solution}')

def get_basin_size(basin_list):
	return len(basin_list[1])

def puzzle2():
	# print(basins)
	sorted_basins = sorted(basins, key = get_basin_size, reverse = True)
	top_3_len = [len(lst) for idx, lst in sorted_basins[:3]]
	solution = prod(top_3_len)
	
	print(f'Puzzle 2 solution: {solution}')

low_points = get_low_points()
basins = get_basins()
display()

puzzle1()
puzzle2()