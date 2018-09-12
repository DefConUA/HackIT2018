1. Global variable is used in alloca call. Make malloc call fail by putting negative size -1, program will simply return but not exit.
2. The global variable gets set however.
3. Overflow in promote()
