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
        n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    if i=="q":
        print("Goodbye!")
        quit = True