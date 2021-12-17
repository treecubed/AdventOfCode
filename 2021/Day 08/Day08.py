def process_line(line):
	line = line.rstrip().split('|')
	line = [sorted([''.join(sorted(x)) for x in line[0].split()], key = len), [''.join(sorted(x)) for x in line[1].split()]]
	return line

with open('input.txt') as file:
	lines = file.readlines()
	data = [process_line(line) for line in lines]

def str_sub(a, b):
	for char in b:
		a = a.replace(char,'')
	return a

def get_decoder(decode_lst):
	def get_key(val):
		for key, value in decode_dict.items():
			if val == value:
				return key
		return None
	seg = {}
	decode_dict = {
		decode_lst.pop(0) : 1,
		decode_lst.pop(0) : 7,
		decode_lst.pop(0) : 4,
		decode_lst.pop(6) : 8
	}
	seg['a'] = str_sub(get_key(7), get_key(1))
	for i in range(3, 6):
		s = str_sub(decode_lst[i], get_key(4) + seg['a'])
		if len(s) == 1:
			seg['g'] = s
			decode_dict[decode_lst.pop(i)] = 9
			break
	seg['e'] = str_sub(get_key(8),get_key(9))
	for i in range(0,3):
		s = str_sub(decode_lst[i], get_key(1) + seg['a'] + seg['g'])
		if len(s) == 1:
			seg['d'] = s
			decode_dict[decode_lst.pop(i)] = 3
			break
	for i in range(0,2):
		s = str_sub(decode_lst[i], seg['a'] + seg['d'] + seg['e'] + seg['g'])
		if len(s) == 1:
			seg['c'] = s
			decode_dict[decode_lst.pop(i)] = 2
			break
	decode_dict[decode_lst.pop(0)] = 5
	for i in range(0,2):
		s = str_sub(decode_lst[i], get_key(5))
		if len(s) == 1:
			decode_dict[decode_lst.pop(i)] = 6
			break
	decode_dict[decode_lst.pop(0)] = 0
	seg['b'] = str_sub(get_key(5), get_key(3))
	seg['f'] = str_sub(get_key(3), get_key(2))
	# print(decode_lst)
	# print(seg, decode_dict)
	return decode_dict

def puzzle1():
	count = 0
	for line in data:
		for digit in line[1]:
			if len(digit) in [2, 3, 4, 7]:
				count += 1
	
	solution = count
	
	print(f'Puzzle 1 solution: {solution}')

def puzzle2():
	lst = []
	for line in data:
		code = ''
		decoder = get_decoder(line[0])
		for char in line[1]:
			code += str(decoder[char])
		lst.append(int(code))
	
	solution = sum(lst)
	
	print(f'Puzzle 2 solution: {solution}')

puzzle1()
puzzle2()