"""
Final-Project.py
Author: Payton
Credit: Python Documentation, Morgan, Mr. Dennison, Stack Overflow
Assignment: Final-Project
Write and submit a program that is your Final Project.
"""
print("Hello, world!")
import binascii
quit = False

while quit == False:
    i = input("Enter a to translate ascii to binary, u to translate Unicode to binary, ba to tranlate binary to ascii, bu to translate binary to Unicode, or q to quit: ")
    if i not in('a', 'u', 'ba', 'bu', 'q'):
        print("Did not understand command, try again.")
        i = input("Enter a to translate ascii to binary, u to translate Unicode to binary (enter all numbers after U+), ba to tranlate binary to ascii, bu to translate binary to Unicode, or q to quit: ")
    if i=="a":
        ascii=input("ascii: ")
        bin2=bin(int(binascii.hexlify(ascii), 16))
        print(bin2)
    if i=="u":
        unic = input("unicode: ")
        print(bin(int(unic, base=16))[2:])
    if i=="ba":
        n = int(input("binary: "), 2)
        binascii.unhexlify('%x' % n)
        sty = str(binascii.unhexlify('%x' % n))
        sty =  str(sty)[:0] + str(sty)[1:]
        print(sty)
    if i=="bu":
        n = int(input("binary: "), 2)
        print(n)
    if i=="q":
        print("Goodbye!")
        quit = True