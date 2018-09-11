Step 1: Reverse the EVM file and figure out the encryption function.

Step 2: Retrieve and Brute force the seed given the SHA-1 Hash & seed.length == 4

Step 3: Use the solve.py to retrieve the half-decrypted hash by implementing decryption routine.

Step 4: Now, implement the custom reverse of ROT-19 encoding which solidity code has implemented. Using online ROT-7 will provide wrong decryption as author has tweaked the ROT-19 Algorithm during encryption process.

Step 5: Append the retrieved plain-text with flag{...} and submit to receive points

Detailed explaination in solve.py file.

flag{patiencepaaysineth}