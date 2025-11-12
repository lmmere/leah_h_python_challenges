def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

print(caesar_cipher("Hello, World!", 3))  # "Khoor, Zruog!"
print(caesar_cipher("Python 3.8", 5))      # "Udtqts 3.8"