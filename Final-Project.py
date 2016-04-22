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
        n = int(input("binary: "), 2)
        binascii.unhexlify('%x' % n)
        #bins23=[]#list(int(n))
        #for r in n:
            #bins23.append(str(r))
       # print(bins23)
       # bin2 = (binascii.b2a_uu(bins23))
       sty = str(binascii.unhexlify('%x' % n))
       sty =  str(sty)[:0] + str(sty)[1:]
        print(sty)
    if i=="q":
        print("Goodbye!")
        quit = True