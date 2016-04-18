"""
Final-Project.py
Author: Payton
Credit: 
Assignment: Final-Project
Write and submit a program that is your Final Project.
"""
import binascii
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
quit = False

while quit == False:
    i = input("Enter t to translate text to binary, b to translate binary to text, or q to quit: ")
    if i not in('t','b','q'):
        print("Did not understand command, try again.")
        i = input("Enter t to translate text to binary, b to translate binary to text, or q to quit: ")
    if i=="t":
        text=input("text: ")
        bin=bin(int(binascii.hexlify(text), 16))
        print(bin)
    if i=="b":
        binary = input(int("binary: ", 2)
        bin2 = binascii.unhexlify(% x % n)
        print(bin2)
    if i=="q":
        print("Goodbye!")
        quit = True