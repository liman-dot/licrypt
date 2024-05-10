"""
Liman. (liman-dot)
Github: liman-dot (github.com/liman-dot/licrypt)
LICENSED under GNU GPLv3
"""
import argparse
import getpass

def flip_with_salt(content, salt):
    salt_bytes = salt.encode()
    salt_length = len(salt_bytes)
    salted_content = bytes([byte ^ salt_bytes[i % salt_length] for i, byte in enumerate(content)])
    return salted_content

def encrypt_file(input_file, output_file, salt):
    try:
        with open(input_file, 'rb') as f:
            content = f.read()
        encrypted_content = flip_with_salt(content, salt)
        with open(output_file, 'wb') as f:
            f.write(encrypted_content)
        print(f"'{input_file}' encrypted and saved as '{output_file}'")
    except FileNotFoundError:
        print(f"{input_file} not found!")

def decrypt_file(input_file, output_file, salt):
    try:
        with open(input_file, 'rb') as f:
            encrypted_content = f.read()
        decrypted_content = flip_with_salt(encrypted_content, salt)
        with open(output_file, 'wb') as f:
            f.write(decrypted_content)
        print(f"'{input_file}' decrypted and saved as '{output_file}'")
    except FileNotFoundError:
        print(f"{input_file} not found!")

def main():
    parser = argparse.ArgumentParser(prog="licrypt", description='Encrypt or decrypt a file using salted flipping method. This is not a safe way to encrypt a file. By Github: LimanGit')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode: encrypt or decrypt')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')
    parser.add_argument('--salt', help='Salt value for encryption/decryption')
    args = parser.parse_args()

    if args.salt:
        salt = args.salt
    else:
        salt = getpass.getpass(prompt='Enter salt: ')

    if args.mode == 'encrypt':
        encrypt_file(args.input_file, args.output_file, salt)
    elif args.mode == 'decrypt':
        decrypt_file(args.input_file, args.output_file, salt)

if __name__ == "__main__":
    main()
