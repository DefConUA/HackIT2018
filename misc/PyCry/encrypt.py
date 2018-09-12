#!/usr/bin/env python
import os
import random,string

#os.chroot('/home/chal/pychal')
#os.setresgid(1003,1003,1003)
#os.setresuid(1003,1003,1003)
def func1e(str1, str2):
	tmp = ""
	for i in range(len(str1)):
		if i%2 == 0 :
			tmp += chr((ord(str1[i])^ord(str2[i])) + 4)
		else:
			tmp += chr((ord(str1[i])^ord(str2[i])) - 2)
	return tmp[::-1]



def func2e(d):
	try:
		k = random.randint(1, 1024)
		n = 0
		f = ""
		for i in range(len(d)):
			n += 1
			c = (n * n) ^ 0x3E
			f += ("00000" + hex(int(oct(ord(d[i]) ^ (k ^ 0xAFE43 ^ 0x399AA3 ^ c))))[2:])[-6:]
		f = (("000" + hex(k ^ 0xA9F ^ 0xE77E)[2:])[-4:] + f)[::-1].upper()
		return f
	except:
		return -1



def func3e(msg, key):
	encryped = []
	for i, c in enumerate(msg):
		key_c = ord(key[i % len(key)])
		msg_c = ord(c)
		encryped.append(chr((msg_c + key_c) % 127))
	return ''.join(encryped)



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


def func4e(str):
	enc = funcwtf(1337)
	return enc(str)


def hint():
	hint = "The flag was encrypted using func2e(func4e(func3e(func1e('flag{redacted}','a6105c0a611b41b08f1209506350279e'),'looooool')))"
	hint += "\nI think the output was : 0A3BFDA6EBFD5CEBFD1ADBFDBEDBFD1DFBFDF10CFD51FBFD51FBFDBEEBFDB3ABFD3DABFD2DABFD589BFDD79BFD9E9BFD10ABFDDFBBFDAFBBFDD4CBFD77CBFD42BBFD91BBFDC2BBFDB4BBFDE7BBFDB6BBFDF0BBFD2ABBFD22BBFD39BBFDE2BBFDB1CE"
	hint += "\nYou guessed right, your goal is to retrieve the flag using your python, reversing and crypto skills"
	hint += "\nGood luck!"
	print hint

def drunkenc():
	encrypted = func2e(func4e(func3e(func1e('flag{redacted}','a6105c0a611b41b08f1209506350279e'),'looooool')))


if __name__ == '__main__':
	name = raw_input("hey bro whats ur name ? : ")
	print "Nice to meet you %s, do  you wanna hack?"%name
	exec(raw_input())
