This Challenge is a python blackbox, where the second user input supplied is directly executed, the script dropped the privileges to a regular user with no read privs, and chrooted so that people do not tamper with ENV variables etc ...  
The idea is basically dump all globals, you will notice the function hint which states explicitly the goal of the challenge which is using dis to reverse the bytecode of each encryption function.   
After rebuilding the original encryption routine, it becomes a trivial crypto problem.
Note: for decryption see decrypt.py
