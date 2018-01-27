import hashlib
from hashlib import md5

#hashed = "757c684714b07c1791c125eb34e5bd15"
begin = "SKY-PWDS-"
m = hashlib.md5()


def hash(inp):
	m = hashlib.md5()
	m.update(inp.encode('utf-8'))
	return m.hexdigest()


hashed = input("Input your md5 hash to be cracked:")
for i in range(10000):
	ans = begin + '%04d' % i
	print(ans)
	if  hash(ans) == hashed:
		print("cracked!")
		break
