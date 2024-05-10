# licrypt

Licrypt is a python script to encrypt and decrypt a file using salt byte flipping method.
# Usage
## Encryption
```bash
licrypt.py --salt SALT encrypt input.txt output.enc
```
## Decryption
```bash
licrypt.py --salt SALT decrypt output.enc output.dec
```
### Info
- --salt is optional argument Don't input salt like this because it will be saved in bash history. Instead putting it will prompt salt input and it will be hidden and it is safe way. (Optional)
- Next is mode. There is 2 lode encrypt and decrypt. (Required)
- Next is input file path for deceyption or encryption. (Required)
- Lastly output file path where it will save the encrypted or decrypted data. (Required)
# Contribution
We'll be happy if you contribute with us. Read CONTRIBUTE.md for more information.
