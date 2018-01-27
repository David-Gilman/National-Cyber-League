import hashlib
from hashlib import md5

begin = "13B"
m = hashlib.md5()


def hash(inp):
	m = hashlib.md5()
	m.update(inp.encode('utf-8'))
	return m.hexdigest()


with open("/Users/davidgilman/Downloads/rockyou.txt", "r") as f:
	for pas in f:
		if  hash(pas)[0:3] == begin:
			print(pas)
			print(hash(pas))
			break
