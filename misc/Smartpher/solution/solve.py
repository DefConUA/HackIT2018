#!/usr/bin/python
'''
Implemented by Aaditya Purani (@aaditya_purani)
There are three functions calling each both are encryption routine.
First function has in-memory array written in inline assembly
In zMx function, it takes plain-text as input checks block.number == 12
Encryption routine in zMx utilizes it and performs calculation along with memory arr
Output is passed to Crp function, which has custom rot-19 implementation
then it is feeded into aXeJ which takes input as bytes and perform require check with seed owner sets
As this is static bytecode, seed cannot be retrieved from bytecode. So we want players to brute seed given sha1 hash & requirements
seed should be exactly 4 length which is given out in one require(bytes(seed).length == 4); checks
Then implement xor checks for aXeJ function
Now, to decrypt implement in reverse given below
'''
cipher = "tphzqh}v}uivyznwju"	# Provided in message.txt
len_cipher = len(cipher)
offset = len_cipher - 2
cipher = list(cipher)
seed = "bcmz"   # Must be retrieved by bruteforce of SHA-1 Hash provided in bytecode 4d64752cadde6ea019757e09ce374aa1bdba81df
cipher[offset] = chr(ord(seed[0]) ^ ord(cipher[offset])^ ord(cipher[offset-2]))
cipher[offset-4] = chr(ord(seed[2]) ^ ord(cipher[offset-4]) ^ ord(cipher[offset-8]))
arr_num = [2, 24, 13, 17,8, 9, 10, 5, 3, 7]     # Must be retrieved carefully from memory array
blk_num = 12
for i in xrange(0, len_cipher):
	cipher[i] = chr((ord(cipher[i])^arr_num[(i+3)%10])^(12))
print "".join(cipher)

# Use the rotcustom.sol to decrypt it further