import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path+'/input/day02_input.txt', 'r')
input_file1 = file.read().split(',')
input_file2 = input_file1.copy()
 
def generate_star(input,i1,i2):
	input = input.copy()
	input[1] = i1
	input[2] = i2
	for pos in range(0,len(input),4):
		if(input[pos] == '1'):
			input_val1 = int(input[pos+1])
			input_val2 = int(input[pos+2])
			loc_val = int(input[pos+3])
			input[loc_val] = int(input[input_val1]) + int(input[input_val2])
		elif(input[pos] == '2'):
			input_val1 = int(input[pos+1])
			input_val2 = int(input[pos+2])
			loc_val = int(input[pos+3])
			input[loc_val] = int(input[input_val1]) * int(input[input_val2])
		elif(input[pos] == '99'):
			return input[0]
			exit

# star 1
print(generate_star(input_file1,12,2))

# star 2
for x in range(0,len(input_file2),1):
	for y in range(0,len(input_file2),1):
		if(generate_star(input_file2,x,y) == 19690720):
			print(100 * x + y)
