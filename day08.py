import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path+'/input/day08_input.txt', 'r')
input_file1 = str(file.read().strip())

row = 0
layer_size = 25*6

layers = []
zero_counts = {}

for i in range(len(input_file1)):
	if((i % (layer_size)) == 0):
		row += 1
	if(int(input_file1[i]) == 0):
		key = 'layer' + str(row)
		if key in zero_counts:
			val = zero_counts[key]
			zero_counts[key] = val + 1
		else:
			zero_counts[key] = 0

l = min(zero_counts, key=zero_counts.__getitem__)
l = int(l[5:])

ones = 0
twos = 0

for i in range(layer_size*(l-1),layer_size*l):
	if(int(input_file1[i]) == 1):
		ones = ones + 1
	elif(int(input_file1[i]) == 2):
		twos = twos + 1

print('\nstar 1: ' + str(ones * twos))

pixels = [[0] * 25 for i in range(6)]

for i in range(0,6):
	for j in range(0,25):
		for k in range(len(zero_counts)):
			if(pixels[i][j] == u'\u2588' or pixels[i][j] == ' '):
				break
			else:
				if(int(input_file1[i*25+j+k*150]) == 0):
					pixels[i][j] = ' '
				elif(int(input_file1[i*25+j+k*150]) == 1):
					pixels[i][j] = u'\u2588'
				elif(int(input_file1[i*25+j+k*150]) == 2):
					pixels[i][j] = '-'

print('star 2:')
for i in range(0,6):
	for j in range(0,25):
		print(pixels[i][j],sep='',end='')
	print('\n')
