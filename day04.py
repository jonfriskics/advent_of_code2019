import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path+'/day04_input.txt', 'r')
input_file1 = file.read().split('-')

r = range(int(input_file1[0]),int(input_file1[1]))

starone_matches = []

for n in r:
	n = str(n)
	if(n[0] == n[1] or n[1] == n[2] or n[2] == n[3] or n[3] == n[4] or n[4] == n[5]):
		if(n[0] <= n[1] and n[1] <= n[2] and n[2] <= n[3] and n[3] <= n[4] and n[4] <= n[5]):
			starone_matches.append(n)

print('star 1: ' + str(len(starone_matches)))

startwo_matches = []

for n in starone_matches:
	n = str(n)
	if((n[0] == n[1] and n[1] != n[2]) or (n[0] != n[1] and n[1] == n[2] and n[2] != n[3]) or (n[1] != n[2] and n[2] == n[3] and n[3] != n[4]) or (n[2] != n[3] and n[3] == n[4] and n[4] != n[5]) or (n[3] != n[4] and n[4] == n[5])):
		startwo_matches.append(n)

print('star 2: ' + str(len(startwo_matches)))
