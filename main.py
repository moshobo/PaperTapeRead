# I created this project to read some old paper tapes.  - July 2nd, 2020
# Here is a useful link on how to read the tapes manually: https://iclces.uk/articles/reading_punched_paper_tape.html
# StackOverflow Help: https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa

def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit

def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(digits=None):
    # Takes in an eight digit binary number. First digit is a parity bit, the rest provide a character.
    # If the sum of the individual digits isn't even, the string will come up as an error

    completestr = ''
    for x in digits:
        if (sum_digits_string(x) % 2) == 0:
            errormsg = ''
        else:
            errormsg = '*Error*'
        digi_chter = x[1:]
        chter = [chr(int(digi_chter, 2))]
        character = ''.join(chter)
        completestr = completestr + errormsg + character

    return completestr

def convertTape(tape):
    # Bits to string
    string = []
    for i in range(0, len(tape), 8):  # len(t1_data)
        char = tape[i:i + 8]
        #zero_char = '0' + char[1:]  # Makes the first digit a zero. Typically first digit would indicate upper/lower case.
        string.append(char)

    finalstring = bits2string(string)

    print('\nYour message reads:')
    print(finalstring)
    return finalstring


# Read in tape data
with open('tape1.txt', 'r') as file:
    t1_data = file.read().replace('\n', '')

with open('tape2.txt', 'r') as file:
    t2_data = file.read().replace('\n', '')

with open('tape3.txt', 'r') as file:
    t3_data = file.read().replace('\n', '')

with open('tape4.txt', 'r') as file:
    t4_data = file.read().replace('\n', '')

with open('tape5.txt', 'r') as file:
    t5_data = file.read().replace('\n', '')

convertTape(t1_data)
convertTape(t2_data)
convertTape(t3_data)
convertTape(t4_data)
convertTape(t5_data)