"""
Final-Project.py
Author: Payton
Credit: 
Assignment: Final-Project
Write and submit a program that is your Final Project.
"""
import binascii
quit = False

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
        n = input((int("binary: "), 2))
        bins23=list(int(n))
        print(bins23)
        bin2 = (binascii.unhexlify('%x' % n))
        print(bin2)
    if i=="q":
        print("Goodbye!")
        quit = True