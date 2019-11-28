import sys
import math


rotor1_position = sys.argv[2]
rotor2_position = sys.argv[3]
rotor3_position = sys.argv[4]
"""
rotor1_position = "a"
rotor2_position = "a"
rotor3_position = "a"
"""

rotor1_default = "rsjwxlopaiztnymudkhefqvgbc"
rotor2_default = "jztnymucrskhdwqibevgxlopaf"
rotor3_default = "opztnymfsjwxludqikhbcrevga"
reflector = "nopqrstuvwxyzabcdefghijklm"

def rotor1_new_position(rotor1_default, letter_selected1):
    rotor1_starting = ""
    for letter in rotor1_default:
        shift = rotor1_default.find(letter_selected1)
        letter_value = rotor1_default.find(letter)
        rotor1_starting += rotor1_default[(letter_value + shift) % 26]
    return rotor1_starting

rotor1_starting = rotor1_new_position(rotor1_default, rotor1_position)
#print(rotor1_new_position(rotor1_default, rotor1_position))

def rotor2_new_position(rotor2_default, letter_selected2):
    rotor2_starting = ""
    for letter in rotor2_default:
        shift = rotor2_default.find(letter_selected2)
        letter_value = rotor2_default.find(letter)
        rotor2_starting += rotor2_default[(letter_value + shift) % 26]
    return rotor2_starting

rotor2_starting = rotor2_new_position(rotor2_default, rotor2_position)
#print(rotor2_new_position(rotor2_default, rotor2_position))

def rotor3_new_position(rotor3_default, letter_selected3):
    rotor3_starting = ""
    for letter in rotor3_default:
        shift = rotor3_default.find(letter_selected3)
        letter_value = rotor3_default.find(letter)
        rotor3_starting += rotor3_default[(letter_value + shift) % 26]
    return rotor3_starting

rotor3_starting = rotor3_new_position(rotor3_default, rotor3_position)
#print(rotor3_new_position(rotor3_default, rotor3_position))

alphabet = "abcdefghijklmnopqrstuvwxyz"

unencrypted_message = sys.argv[1]
#print(unencrypted_message)

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
"""
pair1_letter1 = "a"
pair1_letter2 = "a"
pair2_letter1 = "a"
pair2_letter2 = "a"
pair3_letter1 = "a"
pair3_letter2 = "a"
pair4_letter1 = "a"
pair4_letter2 = "a"
pair5_letter1 = "a"
pair5_letter2 = "a"
pair6_letter1 = "a"
pair6_letter2 = "a"

unencrypted_message = "ujrgb"
print(unencrypted_message)
"""

def enigma_encrypt(unencrypted_message, rotor1_starting, rotor2_starting, rotor3_starting, pair1_letter1, pair1_letter2, pair2_letter1, pair2_letter2, pair3_letter1, pair3_letter2, pair4_letter1, pair4_letter2, pair5_letter1, pair5_letter2, pair6_letter1, pair6_letter2):

    #print(unencrypted_message)
    unencrypted_message_stripped = []
    unencrypted_message_stripped = unencrypted_message.replace(" ", "")
    #print(unencrypted_message_stripped)
    unencrypted_message_stripped_lowercase = []
    unencrypted_message_stripped_lowercase = unencrypted_message_stripped.lower()
    #print(unencrypted_message_stripped_lowercase)
    message_char_list = []
    message_char_list = list(unencrypted_message_stripped_lowercase)
    #print(message_char_list)

    #switch the six pairs of letters

    #first pair of letters
    indices_1_1 = [i for i, x in enumerate(message_char_list) if x == pair1_letter1]
    indices_1_2 = [i for i, x in enumerate(message_char_list) if x == pair1_letter2]

    for i in indices_1_1:
        message_char_list[i] = pair1_letter2

    for i in indices_1_2:
        message_char_list[i] = pair1_letter1

    #second pair of letters
    indices_2_1 = [i for i, x in enumerate(message_char_list) if x == pair2_letter1]
    indices_2_2 = [i for i, x in enumerate(message_char_list) if x == pair2_letter2]

    for i in indices_2_1:
        message_char_list[i] = pair2_letter2

    for i in indices_2_2:
        message_char_list[i] = pair2_letter1

    #third pair of letters
    indices_3_1 = [i for i, x in enumerate(message_char_list) if x == pair3_letter1]
    indices_3_2 = [i for i, x in enumerate(message_char_list) if x == pair3_letter2]

    for i in indices_3_1:
        message_char_list[i] = pair3_letter2

    for i in indices_3_2:
        message_char_list[i] = pair3_letter1

    #fourth pair of letters
    indices_4_1 = [i for i, x in enumerate(message_char_list) if x == pair4_letter1]
    indices_4_2 = [i for i, x in enumerate(message_char_list) if x == pair4_letter2]

    for i in indices_4_1:
        message_char_list[i] = pair4_letter2

    for i in indices_4_2:
        message_char_list[i] = pair4_letter1

    #fifth pair of letters
    indices_5_1 = [i for i, x in enumerate(message_char_list) if x == pair5_letter1]
    indices_5_2 = [i for i, x in enumerate(message_char_list) if x == pair5_letter2]

    for i in indices_5_1:
        message_char_list[i] = pair5_letter2

    for i in indices_5_2:
        message_char_list[i] = pair5_letter1
    #print(message_char_list)

    #sixth pair of letters
    indices_6_1 = [i for i, x in enumerate(message_char_list) if x == pair6_letter1]
    indices_6_2 = [i for i, x in enumerate(message_char_list) if x == pair6_letter2]

    for i in indices_6_1:
        message_char_list[i] = pair6_letter2

    for i in indices_6_2:
        message_char_list[i] = pair6_letter1

    #confirm the six pairs of letters have been switched
    #print(message_char_list)

    #now bring the rotors into play
    rotor2_current = rotor2_starting
    rotor3_current = rotor3_starting
    #message_char_list = split(unencrypted_message)
    encrypted_letters = []
    encrypted_message = ""
    #encrypt each letter in message_char_list one at a time before rotating rotors and encrypting the next letter:
    for i in range(len(message_char_list)):
        #print(message_char_list[i])
        #print(i)
        #first, make sure the rotors are all in the right place
        #rotor1
        rotor1_current = ""
        shift = i
        for char in rotor1_starting:
            char_value = rotor1_starting.find(char)
            rotor1_current += rotor1_starting[(char_value - shift) % 26]
        #print(rotor1_current)
        #rotor2
        rotor2_current = ""
        shift = i
        if (shift % 26 == 0) or (i > 26):
            #print("string should change here")
            for char in rotor2_starting:
                char_value = rotor2_starting.find(char)
                rotor2_current += rotor2_starting[(char_value - math.trunc(i/26)) % 26]
        else:
            rotor2_current = rotor2_starting
        #print(rotor2_current)
        #rotor3
        rotor3_current = ""
        shift = i
        if (shift % 676 == 0) or (i > 676):
            #print("string should change here")
            for char in rotor3_starting:
                char_value = rotor3_starting.find(char)
                rotor3_current += rotor3_starting[(char_value - math.trunc(i/676)) % 26]
        else:
            rotor3_current = rotor3_starting
        #print(rotor3_current)
        #before encrypting, clear the output rotors from the previous encryption
        output_rotor1a = ""
        output_rotor2a = ""
        output_rotor3a = ""
        output_rotor1b = ""
        output_rotor2b = ""
        output_rotor3b = ""
        #encrypt through the first rotor
        letter_value1 = alphabet.find(message_char_list[i])
        output_rotor1a += rotor1_current[letter_value1]
        #print(output_rotor1a)
        #now encrypt through the second rotor
        letter_value2 = alphabet.find(output_rotor1a)
        output_rotor2a += rotor2_current[letter_value2]
        #print(output_rotor2a)
        #and finally encrypt through the third rotor
        letter_value3 = alphabet.find(output_rotor2a)
        output_rotor3a += rotor3_current[letter_value3]
        #print(output_rotor3a)

        #REFLECTOR - this is stationary and sets up to go through the rotors in reverse
        reflector = "nopqrstuvwxyzabcdefghijklm"
        output_reflector = ""
        letter_value_reflector = alphabet.find(output_rotor3a)
        output_reflector += reflector[letter_value_reflector]
        #print(output_reflector)

        #and now go through the rotors in reverse
        #encrypt through the thrid rotor in reverse
        letter_value1 = rotor3_current.find(output_reflector)
        letter_value2 = alphabet[letter_value1]
        #print(letter_value2)

        letter_value3 = rotor2_current.find(letter_value2)
        letter_value4 = alphabet[letter_value3]
        #print(letter_value4)

        letter_value5 = rotor1_current.find(letter_value4)
        letter_value6 = alphabet[letter_value5]
        #print(letter_value6)

        encrypted_letters += letter_value6
    #print("".join(encrypted_letters))

enigma_encrypt(unencrypted_message, rotor1_starting, rotor2_starting, rotor3_starting, pair1_letter1, pair1_letter2, pair2_letter1, pair2_letter2, pair3_letter1, pair3_letter2, pair4_letter1, pair4_letter2, pair5_letter1, pair5_letter2, pair6_letter1, pair6_letter2)
