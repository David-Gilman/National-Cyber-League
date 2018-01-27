inp = "APY-VKUX-9343"
for i in range(0, 27):
	out = ""
	for c in inp:
		if c.isupper():
			out += chr(ord(c)+i)
		else:
			out += c
	print(out)
