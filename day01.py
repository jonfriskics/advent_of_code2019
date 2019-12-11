import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path+'/input/day01_input.txt', 'r')
input = file.read().split('\n')
		
sum_star01 = 0
sum_star02 = 0


def calc_fuel_mass(f,s) -> int:
	m = math.floor((int(f) / 3)) - 2
	if(m <= 0):
		return int(0)
	else:
		return calc_fuel_mass(m,s) + m

for mass in input:
	if(mass != ''):
		sum_star01 += math.floor((int(mass) / 3)) - 2
print('sum_star01 ' + str(sum_star01))

for mass in input:
	if(mass != ''):
		sum_star02 += calc_fuel_mass(mass,sum_star02)
print('sum_star02 ' + str(sum_star02))
