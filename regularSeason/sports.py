import hashlib
from hashlib import md5

m = hashlib.md5()

def hash(inp):
	m = hashlib.md5()
	m.update(inp.encode('utf-8'))
	return m.hexdigest()


f = open("teamlist2", "r")
hashed = input("Input your md5 hash to be cracked:")


for line in f:
	ans = hash(line)
	print(ans)
	if ans == hashed:
		print("cracked!")
		print(ans)
		break

	ans = hash(line[0].upper()+line[1:])
	print(ans)
	if ans == hashed:
		print("cracked!")
		print(ans)
		break

	for i in range(100):
		ans = hash(line + '%04d' % i)
		print(ans)
		if ans == hashed:
			print("cracked!")
			print(ans)
			break

		ans = hash(line[0].upper()+line[1:]+'%04d' % i)
		print(ans)
		if ans == hashed:
			print("cracked!")
			print(ans)
			break
