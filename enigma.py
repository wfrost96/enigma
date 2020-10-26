import sys
import math

rotor1_position = sys.argv[2]
rotor2_position = sys.argv[3]
rotor3_position = sys.argv[4]

rotor1_default = "rsjwxlopaiztnymudkhefqvgbc"
rotor2_default = "jztnymucrskhdwqibevgxlopaf"
rotor3_default = "opztnymfsjwxludqikhbcrevga"
reflector = "nopqrstuvwxyzabcdefghijklm"

def rotor_rotate(rotor_default, letter_selected):
    rotor_starting = ""
    for letter in rotor_default:
        shift = rotor_default.find(letter_selected)
        letter_value = rotor_default.find(letter)
        rotor_starting += rotor_default[(letter_value + shift) % 26]
    return rotor_starting

rotor1_starting = rotor_rotate(rotor1_default, rotor1_position)

rotor2_starting = rotor_rotate(rotor2_default, rotor2_position)

rotor3_starting = rotor_rotate(rotor3_default, rotor3_position)

alphabet = "abcdefghijklmnopqrstuvwxyz"

unencrypted_message = sys.argv[1]

pair1_letter1 = sys.argv[5]
pair1_letter2 = sys.argv[6]
pair2_letter1 = sys.argv[7]
pair2_letter2 = sys.argv[8]
pair3_letter1 = sys.argv[9]
pair3_letter2 = sys.argv[10]
pair4_letter1 = sys.argv[11]
pair4_letter2 = sys.argv[12]
pair5_letter1 = sys.argv[13]
pair5_letter2 = sys.argv[14]
pair6_letter1 = sys.argv[15]
pair6_letter2 = sys.argv[16]

#turn message into string of lowercase characters with all spaces removed
message_char_list = list(unencrypted_message.replace(" ", "").lower())

def switch_letters(letter1, letter2):
    indices_1_1 = [i for i, x in enumerate(message_char_list) if x == letter1]
    indices_1_2 = [i for i, x in enumerate(message_char_list) if x == letter2]
    for i in indices_1_1:
        message_char_list[i] = letter2
    for i in indices_1_2:
        message_char_list[i] = letter1

switch_letters(pair1_letter1, pair1_letter2)
switch_letters(pair2_letter1, pair2_letter2)
switch_letters(pair3_letter1, pair3_letter2)
switch_letters(pair4_letter1, pair4_letter2)
switch_letters(pair5_letter1, pair5_letter2)
switch_letters(pair6_letter1, pair6_letter2)

def enigma_encrypt(unencrypted_message, rotor1_starting, rotor2_starting, rotor3_starting):
    rotor2_current = rotor2_starting
    rotor3_current = rotor3_starting
    encrypted_letters = []
    encrypted_message = ""
    #encrypt each letter in message_char_list one at a time before rotating rotors and encrypting the next letter:
    for i in range(len(message_char_list)):

        #ensure output rotors are empty
        rotor1_current = ""
        rotor2_current = ""
        rotor3_current = ""

        output_rotor1a = ""
        output_rotor2a = ""
        output_rotor3a = ""
        output_rotor1b = ""
        output_rotor2b = ""
        output_rotor3b = ""
        output_reflector = ""

        #set the rotors in the correct position
        shift = i
        #rotor1
        for char in rotor1_starting:
            char_value = rotor1_starting.find(char)
            rotor1_current += rotor1_starting[(char_value - shift) % 26]

        #rotor2
        if (shift % 26 == 0) or (i > 26):
            #print("string should change here")
            for char in rotor2_starting:
                char_value = rotor2_starting.find(char)
                rotor2_current += rotor2_starting[(char_value - math.trunc(i/26)) % 26]
        else:
            rotor2_current = rotor2_starting

        #rotor3
        if (shift % 676 == 0) or (i > 676):
            #print("string should change here")
            for char in rotor3_starting:
                char_value = rotor3_starting.find(char)
                rotor3_current += rotor3_starting[(char_value - math.trunc(i/676)) % 26]
        else:
            rotor3_current = rotor3_starting

        #encrypt through first rotor
        letter_value1 = alphabet.find(message_char_list[i])
        output_rotor1a += rotor1_current[letter_value1]

        #encrypt through second rotor
        letter_value2 = alphabet.find(output_rotor1a)
        output_rotor2a += rotor2_current[letter_value2]

        #encrypt through third rotor
        letter_value3 = alphabet.find(output_rotor2a)
        output_rotor3a += rotor3_current[letter_value3]

        #REFLECTOR - this is stationary and sets up to go through the rotors in reverse
        letter_value_reflector = alphabet.find(output_rotor3a)
        output_reflector += reflector[letter_value_reflector]
        #print(output_reflector)

        #now go through the rotors in reverse
        #encrypt through the third rotor in reverse
        letter_value1 = rotor3_current.find(output_reflector)
        letter_value2 = alphabet[letter_value1]

        letter_value3 = rotor2_current.find(letter_value2)
        letter_value4 = alphabet[letter_value3]

        letter_value5 = rotor1_current.find(letter_value4)
        letter_value6 = alphabet[letter_value5]

        encrypted_letters += letter_value6
    return encrypted_letters

encrypted_letters = enigma_encrypt(unencrypted_message, rotor1_starting, rotor2_starting, rotor3_starting)

#switch letters again
def switch_letters_again(letter1, letter2):
    indices_1_1 = [i for i, x in enumerate(encrypted_letters) if x == letter1]
    indices_1_2 = [i for i, x in enumerate(encrypted_letters) if x == letter2]
    for i in indices_1_1:
        encrypted_letters[i] = letter2
    for i in indices_1_2:
        encrypted_letters[i] = letter1

switch_letters_again(pair1_letter1, pair1_letter2)
switch_letters_again(pair2_letter1, pair2_letter2)
switch_letters_again(pair3_letter1, pair3_letter2)
switch_letters_again(pair4_letter1, pair4_letter2)
switch_letters_again(pair5_letter1, pair5_letter2)
switch_letters_again(pair6_letter1, pair6_letter2)

output = "".join(encrypted_letters)
print(output)
