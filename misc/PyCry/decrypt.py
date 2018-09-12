import string,random

def func3d(encryped, key):
	msg = []
	for i, c in enumerate(encryped):
		key_c = ord(key[i % len(key)])
		enc_c = ord(c)
		msg.append(chr((enc_c - key_c) % 127))
	return ''.join(msg)


def func2d(d):
	try:
		e = d[::-1]
		k = int(e[:4], 16) ^ 0xA9F ^ 0xE77E
		t = e[4:]
		f = ""
		n = 0
		for i in range(0, len(t), 6):
			n += 1
			c = (n * n) ^ 0x3E
			f += chr(int(str(int(t[i:i+6], 16)), 8) ^ (k ^ 0xAFE43 ^ 0x399AA3 ^ c))
		return f
	except:
		return -1

def func4d(str):
	dec = funcwtf(-1337)
	return dec(str)

def funcwtf(n):
	if n > 0:
		n = n % 20
	else :
		n = -((-n) % 20)
	lc = string.ascii_lowercase
	uc = string.ascii_uppercase
	trans = string.maketrans(lc + uc,
                          lc[n:] + lc[:n] + uc[n:] + uc[:n])
	return lambda s: string.translate(s, trans)


def func1d(str1, str2):
	tmp = ""
	str1 = str1[::-1]
	for i in range(len(str1)):
		if i%2 == 0 :
			tmp += chr((ord(str1[i]) - 4)^ord(str2[i]))
		else:
			tmp += chr((ord(str1[i]) + 2)^ord(str2[i]))
	return tmp



print func1d(func3d(func4d(func2d('0A3BFDA6EBFD5CEBFD1ADBFDBEDBFD1DFBFDF10CFD51FBFD51FBFDBEEBFDB3ABFD3DABFD2DABFD589BFDD79BFD9E9BFD10ABFDDFBBFDAFBBFDD4CBFD77CBFD42BBFD91BBFDC2BBFDB4BBFDE7BBFDB6BBFDF0BBFD2ABBFD22BBFD39BBFDE2BBFDB1CE')),'looooool'),'a6105c0a611b41b08f1209506350279e')
