1. Simple UAF exists.

2. The ptr at index=0 can be leaked when printing name.

3. Goal is to make malloc return a libc pointer at index=0.

4. Overwrite global_max_fast using unsorted bin attack (4 bit partial overwrite).

5. Create fastbin chain of size 0x200 and get allocation near mp_struct.

6. Leak libc

7. Determine 5th byte of libc address of \_\_malloc\_hook . 6th byte is assumed to be 0x7f.

8. Do fastbin attack near \_\_malloc\_hook with that size.
