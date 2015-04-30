import re
f = open('jobservice.log')
fout = open('AsyncAmiQ.txt','w')
for line in iter(f):
	if re.search('persist of readings', line):		#find AMRDef Imports
		#fout.write(line)
		subLine = line
		outputLine = ''
		amiHandler = re.findall('handler ([0-9]+)',subLine)	#find Queue number
		for ele in amiHandler:
			#fout.write(ele + '\n')
			outputLine = ele + ' '
		amiDate = re.findall('(....-..-..)',subLine)	#find the Date
		for ele in amiDate:
			outputLine = outputLine + ele + ' '
		amiTime = re.findall('(..:..:..)',subLine)	#find the Time
		for ele in amiTime:
			outputLine = outputLine + ele + ' '
		amiDuration = re.findall('= ([0-9.]+) ms',subLine)	#find the Duration
		for ele in amiDuration:
			outputLine = outputLine + ele
		fout.write(outputLine + '\n')		
f.close
fout.close