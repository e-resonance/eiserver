#sample of import format
#<External name of the channel>,<date>,<GMT Offset>,<Value>,<Code>
#01/01/2014 00:15,4.03200,0,,0.02520,OK,,,,,01/01/2014 08:46:25
#01/01/2014 00:30,3.99600,0,,0.02498,OK,,,,,01/01/2014 08:46:25
import re
mode = input('File mode to use a or w: ')
chanExtId = input('Enter the Channel External ID: ')
gmtOffset = input('Enter the gmt offset code: ')
file2open = input('Enter the file to open: ')
f = open(file2open)
fout = open('intReadings.csv', mode)
for line in iter(f):
	if re.search('^../../.... ..:..,', line):		#find the interval data lines
		subLine = line
		outputLine = ''
		intDateTime = re.findall('^(../../.... ..:..),',subLine)	#find date and time
		for ele in intDateTime:
			outputLine = chanExtId + ',' + ele + ',' + gmtOffset + ',' 
		intValue = re.findall('^../../.... ..:..,([0-9.]+)[0-9][0-9],',subLine)	#find the interval reading
		for ele in intValue:
			outputLine = outputLine + ele + ',0' 	
		fout.write(outputLine + '\n')
f.close
fout.close