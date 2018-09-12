1. Off by one allows us to change size.

2. Need to make sure to leak using the read() function , and not fgets().

3. Leak .text, control array of heap_ptrs.

4. Perform fastbin attack near \_\_free\_hook - 0x1000, write ptr to address which contains the money check.

5. Make heap_ptr in .text point to \_\_free\_hook - 0x1000 so that the money check passes successfully.

6. Use edit, it will allow you to write unlimited bytes, and reach \_\_free\_hook.
