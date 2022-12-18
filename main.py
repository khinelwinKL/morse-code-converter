import os

ENG_TO_MORSE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                     'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                     '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '}

MORSE_TO_ENG_DICT = {}
for key, value in ENG_TO_MORSE_DICT.items():
    MORSE_TO_ENG_DICT[value] = key


def eng_to_morse(message):
    morse_code = ""
    for char in message.upper():
        if char != " ":
            morse_code += ENG_TO_MORSE_DICT[char] + " "
        else:
            morse_code += " "
    return morse_code


def morse_to_eng(message_code):
    message_code += " "
    result = ""
    code = ""
    i = 0
    for char in message_code:
        if char != " ":
            i = 0
            code += char
        else:
            i += 1
            if i == 2:
                result += " "
            else:
                result += MORSE_TO_ENG_DICT[code]
                code = ""
    return result


game_end = False
while not game_end:
    os.system("cls")
    mode = input("Type 'encode' to convert english to morse code or 'decode' to convert morse code to english: ")
    if mode.lower() == "encode":
        word = input("Please enter the word you want to encode: ")
        encoded_message = eng_to_morse(word)
        print(f"The encoded message: {encoded_message}")
    else:
        word = input("Please enter the code you want to decode: ")
        decoded_message = morse_to_eng(word)
        print(f"The decoded message: {decoded_message}")

    restart_game = input("Do you want to convert more message? Please enter 'yes' or 'no': ")
    if restart_game.lower() == "no":
        game_end = True
        print("Thank you for using our service. Have a nice day!")
    else:
        game_end = False




