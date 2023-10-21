# Define Morse code mappings
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(char)
    return ' '.join(morse_code)

def morse_to_text(morse_code):
    morse_code = morse_code.split()
    text = []
    for code in morse_code:
        if code in morse_code_dict.values():
            text.append(list(morse_code_dict.keys())[list(morse_code_dict.values()).index(code)])
        else:
            text.append(code)
    return ''.join(text)

print("Morse Code Translator")
print("1. English to Morse Code")
print("2. Morse Code to English")
choice = int(input("Enter your choice: "))

if choice == 1:
    english_text = input("Enter English text: ")
    morse_result = text_to_morse(english_text)
    print("Morse code:", morse_result)
elif choice == 2:
    morse_code = input("Enter Morse code: ")
    text_result = morse_to_text(morse_code)
    print("English text:", text_result)
else:
    print("Invalid choice. Please select 1 for English to Morse Code or 2 for Morse Code to English.")
