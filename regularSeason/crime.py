from datetime import datetime
import time
from datetime import date

access = open("access.log", "r")
badge = open("badge.log", "r")

class Session(object):
	name = ""
	timebegin = datetime.today()
	timeend = datetime(2009, 10, 5, 18, 00)
	delta = timeend-timebegin

	def __init__(self, name, timebegin):
		self.name = name
		self.timebegin = timebegin
	

	def getDelta():
		delta = timeend-timebegin


sessions = []

for line in badge:
	name = line.split()[2]+line.split()[3]
	clock = datetime.strptime(line.split()[0]+" "+line.split()[1], "%Y-%m-%d %H:%M:%S")
	if line.split()[5] == "In":
		sessions.append(Session(name,clock))
	elif line.split()[5] == "Out":
		for i in range(len(sessions)):
			if sessions[i].name == name and sessions[i].timeend == datetime(2009, 10, 5, 18, 00):
				sessions[i].timeend = clock
	else:
		print(line)


'''
for x in sessions:
	if x.timeend == datetime(2009, 10, 5, 18, 00):
		print("!!!" + x.name + " " + x.timebegin.strftime('%m/%d/%Y'))
	else:
'''
		print(x.name + " " + x.timebegin.strftime('%m/%d/%Y')) 
