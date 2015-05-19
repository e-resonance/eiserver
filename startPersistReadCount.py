import re
mode = input('File mode to use a or w: ')
logDate = input('Date to extract (YYYY-MM-DD): ')
f = open('jobservice.log')
fout = open('AsyncAmiQReadCount.txt', mode)
for line in iter(f):
	if re.search(logDate + '.* Starting persist', line):		#find RTU and RTURegister Caches
		subLine = line
		outputLine = ''
		amiHandler = re.findall('handler ([0-9]+)',subLine)	#find Queue number
		for ele in amiHandler:
			outputLine = ele + ' '
		amiDate = re.findall('(' + logDate + ')',subLine) #find the Date
		for ele in amiDate:
			outputLine = outputLine + ele + ' '
		amiTime = re.findall('(..:..:..)',subLine)	#find the Time
		for ele in amiTime:
			outputLine = outputLine + ele + ' '
		readCount = re.findall('Starting persist of ([0-9]+) readings',subLine)	#find the Read Count
		for ele in readCount:
			outputLine = outputLine + ele
		fout.write(outputLine + '\n')	#file format is: Queue 	Datestamp Timestamp Read Count
f.close
fout.close