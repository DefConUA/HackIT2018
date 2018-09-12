1. Uninitialised variable exists in linked list, but not exploitable since program uses calloc.

2. Use xoring to change last nibble of calloc to 0xf.

3. Now , calloc will not perform the zero-ing operation, and result in creating the bug "uninitialized FD ptr of linked list".

4. Calloc trick I learnt from Stringer (RCTF, an XCTF league event).
