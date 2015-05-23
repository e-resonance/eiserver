#sample of import format
#Wed May 20 20:05:36 CDT 2015;EisReport;kWh Delivered - Current - Tier D;1;0.000;Fri Mar 23 04:00:00 CDT 2012;null;Fri Mar 23 04:00:00 CDT 2012;null;null;null;null;1;com.energyict.mdw.amr.RtuRegisterReadingFlags@3c6d1e82;null;null;null;ok;0;DCGROUP;2012-03-23 04:46:08.0;1 / null;true;0;03/23/2012 04:00:00;null;03/23/2012 04:00:00;null;null;1;Valid;OK;03/23/2012 04:46:08
import re
mode = input('File mode to use a or w: ')
rtuExtId = input('Enter the RTU External ID: ')
obisCode = input('Enter the OBIS code: ')
register = input('Enter the name of the register to extract: ')
f = open('registerRead.csv')
fout = open('regReadings.csv', mode)
for line in iter(f):
	if re.search('EisReport;' + register, line):		#find the correct register
		subLine = line
		outputLine = ''
		regRead = re.findall(register + ';([0-9.]+)',subLine)	#find register reading
		for ele in regRead:
			outputLine = rtuExtId + ';' + obisCode + ';' + ele + ';;' #leaving the register advance blank so that it is calculated on import
			
			
			
		readTimeMonth = re.findall(register + ';[0-9]+;[0-9.]+;... (...)'  ,subLine) #find the read time month
		for ele in readTime:
			outputLine = outputLine + ele + ' '
			
			
			
			
#		amiTime = re.findall('(..:..:..)',subLine)	#find the Time
#		for ele in amiTime:
#			outputLine = outputLine + ele + ' '
#		amiDuration = re.findall('took ([0-9.]+) ms',subLine)	#find the Duration
#		for ele in amiDuration:
#			outputLine = outputLine + ele
		fout.write(outputLine + '\n')
f.close
fout.close