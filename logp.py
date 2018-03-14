#This is a simple log parser I designed - this basically calculates depth and prints out contents of if and else statements based off on the input list (list of defines)


import re

f = open("log.txt")
 
# read all the lines in the file and return them in a list
lines = f.readlines()

#print(lines)


count=0

regex = 'ifdef\s([_a-fA-F]+)'
defs = {}
input = []
input.append('def_A')
inputset = set(input)
#find all ifdefs in the file and create a dictionary
for line in lines:
	#print(line)
	match = re.search(regex,line)
	if match:
		defs[match.group(1)] = 0;
		#print(match.group(1))

#print(defs)

#for line in lines:
for i in range (0,len(lines)):
#	print(lines[i])
	if (lines[i].find("ifdef")>0):
		count+=1
		match = re.search(regex,lines[i])
		defs[match.group(1)] = count
		last_match = match.group(1)
		if last_match in inputset:
			print(lines[(i+1)%len(lines)])
	elif (lines[i].find("else")>0):
		count-=1
	#	print("********")
	#	print(lines[i])
	#	print(defs[last_match])
	#	print(count)
	#	print("********")
		if((defs[last_match]-count) == 1):
			print(lines[i+1])

#print(defs)






