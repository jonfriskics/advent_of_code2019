import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path+'/day03_input.txt', 'r')
input_file1 = file.read().split('\n')

count = 0
coords1 = set()
coords2 = set()

for line in input_file1:
	steps = line.split(',')
	x = 0
	y = 0
	for step in steps:
		if(step != ''):
			direction = step[0]
			value = step[1:]
			for n in range(int(value)):
				if(direction == 'U'):
					y += 1
				elif(direction == 'D'):
					y -= 1
				elif(direction == 'L'):
					x -= 1
				elif(direction == 'R'):
					x += 1
				if(count == 0):
					coords1.add((x,y))
				elif(count == 1):
					coords2.add((x,y))
	count += 1

intersect = coords1.intersection(coords2)

def manhatten_distance(x,y):
	return sum(abs(a-b) for a,b in zip(x,y))

distances = []
for coord in intersect:
	md = manhatten_distance([0,0],[coord[0],coord[1]])
	distances.append(md)

print('star 1: ' + str(min(sorted(distances))))

line1_counts = []
line2_counts = []
count = 0
broken = 0

for i in intersect:
	for line in input_file1:
		steps = line.split(',')
		step_taken = 0
		x = 0
		y = 0
		for step in steps:
			if(step != ''):
				direction = step[0]
				value = step[1:]
				for n in range(int(value)):
					if(direction == 'U'):
						y += 1
						step_taken += 1
					elif(direction == 'D'):
						y -= 1
						step_taken += 1
					elif(direction == 'L'):
						x -= 1
						step_taken += 1
					elif(direction == 'R'):
						x += 1
						step_taken += 1
					if(x == i[0] and y == i[1]):
						if(count == 0):
							line1_counts.append(step_taken)
						elif(count == 1):
							line2_counts.append(step_taken)
		count += 1
	count = 0

sum_of_line_counts = []
for index, value in enumerate(line1_counts):
	sum_of_line_counts.append(line1_counts[index] + line2_counts[index])

print('star 2: ' + str(min(sum_of_line_counts)))
