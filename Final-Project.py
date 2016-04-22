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
        n = input("binary:") #input((int("binary: "), 2))
        bins23=[]#list(int(n))
        for r in n:
            bins23.append(int(r))
        print(bins23)
        bin2 = (binascii.b2a_uu('%x' % n))
        print(bin2)
    if i=="q":
        print("Goodbye!")
        quit = True