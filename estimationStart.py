import re
f = open('jobservice.log')
fout = open('AsyncAmiQEstimationStart.txt','w')
for line in iter(f):
	if re.search('Estimation.*Starting analysis for task', line):		#find estimation start entries
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
			outputLine = outputLine + ele + ';0;'
		estimationGroup = re.findall('for task \'(.*)\' on JobQueue',subLine)	#find the Estimation Group
		for ele in estimationGroup:
			outputLine = outputLine + ele + ';'
		estimationStart = re.findall('for period From (.*) to',subLine)	#find the Estimation From
		for ele in estimationStart:
			outputLine = outputLine + ele + ';'
		estimationStop = re.findall(' to (.*)\n',subLine)	#find the Estimation To
		for ele in estimationStop:
			outputLine = outputLine + ele
		fout.write(outputLine + '\n')	#file format is: Queue;Datestamp;Timestamp;0;Estimation Group;Estimation From;Estimation To 
f.close
fout.close