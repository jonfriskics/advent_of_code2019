import os
import math

dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path+'/input/day05_input.txt', 'r')
input_file1 = file.read().split(',')
input_file2 = input_file1.copy()
opcodes = list(map(int, input_file1))

system_id = [1]

def parse_opcode(i):
  op = str(i)
  opcode_length = len(str(i))
  
  opcode = 0
  param1_mode = 0
  param2_mode = 0
  param3_mode = 0
  
  if(opcode_length == 1):
    opcode = int(op)
  elif(opcode_length == 2):
    opcode = int(op)
  elif(opcode_length == 3):
    opcode = int(op[1:])
    param1_mode = int(op[0])
  elif(opcode_length == 4):
    opcode = int(op[2:])
    param1_mode = int(op[1])
    param2_mode = int(op[0])
  elif(opcode_length == 5):
    opcode = int(op[3:])
    param1_mode = int(op[2])
    param2_mode = int(op[1])
    param3_mode = int(op[0])
  return (opcode, param1_mode, param2_mode, param3_mode)

def generate_star(input, system_id):
  input = input.copy()

  pos = 0
    
  while(pos < len(opcodes)):
    opcode = parse_opcode(input[pos])
    
    if(opcode[0] == 1):
      param1 = int(input[pos+1])
      param2 = int(input[pos+2])
      param3 = int(input[pos+3])
      val1 = 0
      val2 = 0

      if(opcode[1] == 0):
        val1 = int(input[param1])
      elif(opcode[1] == 1):
        val1 = param1
      
      if(opcode[2] == 0):
        val2 = int(input[param2])
      elif(opcode[2] == 1):
        val2 = param2
            
      input[param3] = val1 + val2

      pos += 4
    elif(opcode[0] == 2):
      param1 = int(input[pos+1])
      param2 = int(input[pos+2])
      param3 = int(input[pos+3])
      val1 = 0
      val2 = 0
            
      if(opcode[1] == 0):
        val1 = int(input[param1])
      elif(opcode[1] == 1):
        val1 = param1
      
      if(opcode[2] == 0):
        val2 = int(input[param2])
      elif(opcode[2] == 1):
        val2 = param2

      input[param3] = val1 * val2

      pos += 4
    elif(opcode[0] == 3):
      param1 = int(input[pos+1])
      val1 = 0
      
      if(opcode[1] == 0):
        val1 = int(input[param1])
      elif(opcode[1] == 1):
        val1 = param1

      input[param1] = system_id[0]

      pos += 2
    elif(opcode[0] == 4):
      param1 = int(input[pos+1])
      val1 = 0
      
      if(opcode[1] == 0):
        val1 = int(input[param1])
      elif(opcode[1] == 1):
        val1 = param1
        
      print(val1)
      
      pos += 2
    elif(opcode[0] == 5):
      param1 = int(input[pos+1])
      param2 = int(input[pos+2])
      val1 = 0
      val2 = 0
      
      if(opcode[1] == 0):
        val1 = int(input[param1])
      elif(opcode[1] == 1):
        val1 = param1
      
      if(opcode[2] == 0):
        val2 = int(input[param2])
      elif(opcode[2] == 1):
        val2 = param2
      
      if(val1 != 0):
        pos = val2
      else:
        pos += 3
    elif(opcode[0] == 6):
      param1 = int(input[pos+1])
      param2 = int(input[pos+2])
      val1 = 0
      val2 = 0
      
      if(opcode[1] == 0):
        val1 = int(input[param1])
      elif(opcode[1] == 1):
        val1 = param1
      
      if(opcode[2] == 0):
        val2 = int(input[param2])
      elif(opcode[2] == 1):
        val2 = param2
        
      if(val1 == 0):
        pos = val2
      else:			
        pos += 3
    elif(opcode[0] == 7):
      param1 = int(input[pos+1])
      param2 = int(input[pos+2])
      param3 = int(input[pos+3])
      val1 = 0
      val2 = 0
      
      if(opcode[1] == 0):
        val1 = int(input[param1])
      elif(opcode[1] == 1):
        val1 = param1
      
      if(opcode[2] == 0):
        val2 = int(input[param2])
      elif(opcode[2] == 1):
        val2 = param2

      if(val1 < val2):
        input[param3] = 1
      else:
        input[param3] = 0
        
      pos += 4
    elif(opcode[0] == 8):
      param1 = int(input[pos+1])
      param2 = int(input[pos+2])
      param3 = int(input[pos+3])
      val1 = 0
      val2 = 0

      if(opcode[1] == 0):
        val1 = int(input[param1])
      elif(opcode[1] == 1):
        val1 = param1
      
      if(opcode[2] == 0):
        val2 = int(input[param2])
      elif(opcode[2] == 1):
        val2 = param2

      if(val1 == val2):
        input[param3] = 1
      else:
        input[param3] = 0
        
      pos += 4
    elif(opcode[0] == 99):
      break
  return input[0]

print('\n')
generate_star(input_file1, [1])
generate_star(input_file1, [5])
