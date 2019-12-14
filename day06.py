import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path+'/input/day06_input.txt', 'r')
input_file1 = file.read().strip()

orbit_pairs = input_file1.split()

orbits = []
for orbit in orbit_pairs:
  orbit1 = orbit.split(')')[0]
  orbit2 = orbit.split(')')[1]
  orbits.append([orbit1, orbit2])

orbit_pairs = {}
for orbit in orbits:
  orbit_pairs[orbit[1]] = orbit[0]

total = 0

for orbitee in orbit_pairs:
  while orbitee != "COM":
    orbitee = orbit_pairs[orbitee]
    total += 1

print('star 1: ' + str(total))

start = orbit_pairs['YOU']
destination = orbit_pairs['SAN']

starts = [start]
while starts[len(starts)-1] != "COM":
  starts.append(orbit_pairs[starts[len(starts)-1]])

ends = [destination]
while ends[len(ends)-1]!="COM":
  ends.append(orbit_pairs[ends[len(ends)-1]])

while starts and ends and starts[len(starts)-1]==ends[len(ends)-1]:
  starts.pop(len(starts)-1)
  ends.pop(len(ends)-1)

print('star 2: ' + str(len(starts) + len(ends)))