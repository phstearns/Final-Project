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
    i = input("Enter e to translate text to binary, d to translate binary to text, or q to quit: ")
    if i not in('t','b','q'):
        print("Did not understand command, try again.")
        i = input("Enter t to translate text to binary, b to translate binary to text, or q to quit: ")
    if i=="t":
        text=input("text: ")
        bin(int(binascii.hexlify(text), 16))
        let=[]
        kelt=[]
        comb =[]
        if m>k:
            count = key * int((m-(m%k))/k)
            trun = key[0:(m%k)]
            newkey = count + trun
        elif k>m:
            newkey = key[0:m] 
            print(newkey, message)
        for x in range (0,m):
            let.append(associations.find(message[x]))
        for y in range (0,m):
            kelt.append(associations.find(newkey[y]))
        for c in range (0,len(kelt)):
            r = (let[c] + kelt[c]) % 85
            comb.append(associations[r])
        print("".join([x for x in comb]), end="")
        print()
    if i=="b":
        kelt=[]
        let=[]
        comb=[]
        binary=input("binary: ")
        if m>k:
            count = key * int((m-(m%k))/k)
            trun = key[0:(m%k)]
            newkey = count + trun
        elif k>m:
            newkey = key[0:m] 
            print(newkey, message)
        for x in range (0,m):
            let.append(associations.find(message[x]))
        for y in range (0,m):
            kelt.append(associations.find(newkey[y]))
        for c in range (0,len(kelt)):
            r = (let[c] - kelt[c]) % 85
            comb.append(associations[r])
        print("".join([x for x in comb]), end="")
        print()
    if i=="q":
        print("Goodbye!")
        quit = True