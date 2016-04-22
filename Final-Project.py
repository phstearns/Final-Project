"""
Final-Project.py
Author: Payton
Credit: 
Assignment: Final-Project
Write and submit a program that is your Final Project.
"""
import binascii
quit = False

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

while quit == False:
    i = input("Enter a to translate ascii to binary, b to translate binary to ascii, or q to quit: ")
    if i not in('a','b','q'):
        print("Did not understand command, try again.")
        i = input("Enter a to translate ascii to binary, b to translate binary to ascii, or q to quit: ")
    if i=="a":
        ascii=input("ascii: ")
        bin=bin(int(binascii.hexlify(ascii), 16))
        print(bin)
    if i=="b":
        #n = input("binary: ")
        #n = int('0b110100001100101011011000110110001101111', 2)
        #n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
        
        #bins23=[]#list(int(n))
        #for r in n:
            #bins23.append(str(r))
       # print(bins23)
       # bin2 = (binascii.b2a_uu(bins23))
        print(text_from_bits('110100001100101011011000110110001101111'))
    if i=="q":
        print("Goodbye!")
        quit = True