def vigenere_cipher(message, key, operation):
    key = key.upper()
    result = []

    for i in range(len(message)):
        if message[i].isalpha():
            key_char = key[i % len(key)]
            shift = ord(key_char) - ord('A') if key_char.isalpha() else 0

            if operation == 1:  # Encryption
                char_code = ord(message[i]) + shift
                if message[i].islower():
                    if char_code > ord('z'):
                        char_code -= 26
                elif message[i].isupper():
                    if char_code > ord('Z'):
                        char_code -= 26
            elif operation == 2:  # Decryption
                char_code = ord(message[i]) - shift
                if message[i].islower():
                    if char_code < ord('a'):
                        char_code += 26
                elif message[i].isupper():
                    if char_code < ord('A'):
                        char_code += 26

            result.append(chr(char_code))
        else:
            result.append(message[i])

    return ''.join(result)

message = input("Enter a message: ")
key = input("Enter a key: ").upper()

print("Choose an operation:")
print("1. Encrypt")
print("2. Decrypt")
operation = int(input())

if operation == 1:
    encrypted_message = vigenere_cipher(message, key, 1)
    print("Encrypted message:", encrypted_message)
elif operation == 2:
    decrypted_message = vigenere_cipher(message, key, 2)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid operation choice. Please choose 1 for encryption or 2 for decryption.")
