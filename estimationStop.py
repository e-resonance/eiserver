import re
f = open('jobservice.log')
fout = open('AsyncAmiQEstimationStop.txt','w')
for line in iter(f):
	if re.search('Estimation.*Finished default action', line):		#find estimation start entries
		subLine = line
		outputLine = ''
		amiHandler = re.findall('thread ([0-9]+)',subLine)	#find Queue number
		for ele in amiHandler:
			outputLine = ele + ';'
		amiDate = re.findall('\[(....-..-..)',subLine)	#find the Date
		for ele in amiDate:
			outputLine = outputLine + ele + ';'
		amiTime = re.findall('(..:..:..),',subLine)	#find the Time
		for ele in amiTime:
			outputLine = outputLine + ele + ';'
		message = re.findall('Actions\) - (.*)\n',subLine)	#find the Estimation Finished Message
		for ele in message:
			outputLine = outputLine + ele
		fout.write(outputLine + '\n')	#file format is: Queue;Datestamp;Timestamp;Message 
f.close
fout.close