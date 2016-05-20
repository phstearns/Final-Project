"""
Final-Project.py
Author: Payton
Credit: Python Documentation, Morgan, Mr. Dennison, Stack Overflow
Assignment: Final-Project
Write and submit a program that is your Final Project.
"""
import binascii
quit = False

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

while quit == False:
    i = input("Enter a to translate ascii to binary, u to translate Unicode to binary, ba to tranlate binary to ascii, bu to translate binary to Unicode, or q to quit: ")
    if i not in('a', 'u', 'ba', 'bu', 'q'):
        print("Did not understand command, try again.")
        i = input("Enter a to translate ascii to binary, u to translate Unicode to binary, ba to tranlate binary to ascii, bu to translate binary to Unicode, or q to quit: ")
    if i=="a":
        ascii=input("ascii: ")
        bin2=bin(int(binascii.hexlify(ascii), 16))
        print(bin2)
    if i=="u":
        #unic = input("unicode: ")
        #byt2 = bytearray(hex=unic)
        #byt2 = bin(int('ff', base=16))[2:]
       # byt3 = bin(int(byt2)) 
        print(bin(int('ff', base=16))[2:])
    if i=="ba":
        n = int(input("binary: "), 2)
        binascii.unhexlify('%x' % n)
        sty = str(binascii.unhexlify('%x' % n))
        sty =  str(sty)[:0] + str(sty)[1:]
        print(sty)
    """
    if i=="bu":
        n = int(input(binary: "), 2)
        
    """
    if i=="q":
        print("Goodbye!")
        quit = True