mess_out = []
mess_in = ''

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  ' ': ' '
}

mess_in = str(input("Enter the sentence: "))
mess_in = mess_in.upper()

coding = int(input("Enter 1 for Coding or 0 for Decoding: "))
coding = True if coding == 1 else False

if coding:
    for mess in mess_in:
        try:
            x = CODE[mess]
        except KeyError:
            x = " "
        mess_out.append(x)

    print(" ".join(mess_out))

else:
    mess_in = mess_in.split(" ")  
    for mess in mess_in:
        for key, value in CODE.items():
            if mess == value:
                mess_out.append(key)
                break
    print("".join(mess_out))        