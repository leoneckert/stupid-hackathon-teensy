import sys

counter= 0
print "char Str2[1164] = {"
for line in sys.stdin:
	line = line.strip();
	# print line
	for c in line:
		if c == "'":
			print "'\\"+c+"', "
		else:
			print "'"+c+"', "
		counter = counter + 1
	# 	print "Keyboard.print(\"" + c + "\");"
	print "'\\n', "
	counter = counter + 1
print "};"
print counter

