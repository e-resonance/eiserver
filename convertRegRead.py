#sample of import format
#Wed May 20 20:05:36 CDT 2015;EisReport;kWh Delivered - Current - Tier D;1;0.000;Fri Mar 23 04:00:00 CDT 2012;null;Fri Mar 23 04:00:00 CDT 2012;null;null;null;null;1;com.energyict.mdw.amr.RtuRegisterReadingFlags@3c6d1e82;null;null;null;ok;0;DCGROUP;2012-03-23 04:46:08.0;1 / null;true;0;03/23/2012 04:00:00;null;03/23/2012 04:00:00;null;null;1;Valid;OK;03/23/2012 04:46:08
import re
mode = input('File mode to use a or w: ')
rtuExtId = input('Enter the RTU External ID: ')
obisCode = input('Enter the OBIS code: ')
register = input('Enter the name of the register to extract: ')
file2open = input('Enter the file to open: ')
f = open(file2open)
fout = open('regReadings.csv', mode)
for line in iter(f):
	if re.search('EisReport;' + register, line):		#find the correct register
		subLine = line
		outputLine = ''
		regRead = re.findall(register + ';[0-9]+;([0-9.]+)',subLine)	#find register reading
		for ele in regRead:
			outputLine = rtuExtId + ';' + obisCode + ';' + ele + ';;' #leaving the register advance blank so that it is calculated on import
			
		readTimeYear = re.findall(register + ';[0-9]+;[0-9.]+;... ... .. ..:..:.. ... (....)',subLine) #find the read time year	
		for ele in readTimeYear:
			outputLine = outputLine + ele + '/'
			
		readTimeMonth = re.findall(register + ';[0-9]+;[0-9.]+;... (...)',subLine) #find the read time month
		for ele in readTimeMonth:
			if ele=='Jan':
				ele='01'
			elif ele=='Feb':
				ele='02'
			elif ele=='Mar':
				ele='03'
			elif ele=='Apr':
				ele='04'
			elif ele=='May':
				ele='05'
			elif ele=='Jun':
				ele='06'
			elif ele=='Jul':
				ele='07'
			elif ele=='Aug':
				ele='08'
			elif ele=='Sep':
				ele='09'
			elif ele=='Oct':
				ele='10'
			elif ele=='Nov':
				ele='11'
			elif ele=='Dec':
				ele='12'
			else:
				ele=''
			outputLine = outputLine + ele + '/'
			
		readTimeDay = re.findall(register + ';[0-9]+;[0-9.]+;... ... (..)',subLine) #find the read time day
		for ele in readTimeDay:
			outputLine = outputLine + ele + ' '
			
		readTime = re.findall(register + ';[0-9]+;[0-9.]+;... ... .. (..:..:..)',subLine) #find the read time
		for ele in readTime:
			outputLine = outputLine + ele + ';;;'
			
			
#		eventTimeYear = re.findall(register + ';[0-9]+;[0-9.]+;... ... .. ..:..:.. ... (....)',subLine) #find the read time year	
#		for ele in eventTimeYear:
#			outputLine = outputLine + ele + '/'
			
#		eventTimeMonth = re.findall(register + ';[0-9]+;[0-9.]+;... (...)',subLine) #find the read time month
#		for ele in eventTimeMonth:
#			if ele=='Jan':
#				ele='01'
#			elif ele=='Feb':
#				ele='02'
#			elif ele=='Mar':
#				ele='03'
#			elif ele=='Apr':
#				ele='04'
#			elif ele=='May':
#				ele='05'
#			elif ele=='Jun':
#				ele='06'
#			elif ele=='Jul':
#				ele='07'
#			elif ele=='Aug':
#				ele='08'
#			elif ele=='Sep':
#				ele='09'
#			elif ele=='Oct':
#				ele='10'
#			elif ele=='Nov':
#				ele='11'
#			elif ele=='Dec':
#				ele='12'
#			else:
#				ele=''
#			outputLine = outputLine + ele + '/'
			
#		eventTimeDay = re.findall(register + ';[0-9]+;[0-9.]+;... ... (..)',subLine) #find the read time day
#		for ele in eventTimeDay:
#			outputLine = outputLine + ele + ' '
			
#		eventTime = re.findall(register + ';[0-9]+;[0-9.]+;... ... .. (..:..:..)',subLine) #find the read time
#		for ele in eventTime:
#			outputLine = outputLine + ele + ';'			


		toTimeYear = re.findall(register + ';[0-9]+;[0-9.]+;... ... .. ..:..:.. ... ....;null;... ... .. ..:..:.. ... (....)',subLine) #find the from time year	
		for ele in toTimeYear:
			outputLine = outputLine + ele + '/'
			
		toTimeMonth = re.findall(register + ';[0-9]+;[0-9.]+;... ... .. ..:..:.. ... ....;null;... (...)',subLine) #find the from time month
		for ele in toTimeMonth:
			if ele=='Jan':
				ele='01'
			elif ele=='Feb':
				ele='02'
			elif ele=='Mar':
				ele='03'
			elif ele=='Apr':
				ele='04'
			elif ele=='May':
				ele='05'
			elif ele=='Jun':
				ele='06'
			elif ele=='Jul':
				ele='07'
			elif ele=='Aug':
				ele='08'
			elif ele=='Sep':
				ele='09'
			elif ele=='Oct':
				ele='10'
			elif ele=='Nov':
				ele='11'
			elif ele=='Dec':
				ele='12'
			else:
				ele=''
			outputLine = outputLine + ele + '/'
			
		toTimeDay = re.findall(register + ';[0-9]+;[0-9.]+;... ... .. ..:..:.. ... ....;null;... ... (..)',subLine) #find the from time day
		for ele in toTimeDay:
			outputLine = outputLine + ele + ' '
			
		toTime = re.findall(register + ';[0-9]+;[0-9.]+;... ... .. ..:..:.. ... ....;null;... ... .. (..:..:..)',subLine) #find the from time
		for ele in toTime:
			outputLine = outputLine + ele + ';0;1;;'	


			
#		amiTime = re.findall('(..:..:..)',subLine)	#find the Time
#		for ele in amiTime:
#			outputLine = outputLine + ele + ' '
#		amiDuration = re.findall('took ([0-9.]+) ms',subLine)	#find the Duration
#		for ele in amiDuration:
#			outputLine = outputLine + ele
		fout.write(outputLine + '\n')
f.close
fout.close