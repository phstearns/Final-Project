"""
Final-Project.py
Author: Payton
Credit: 
Assignment: Final-Project
Write and submit a program that is your Final Project.
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
quit = False

while quit == False:
    i = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if i not in('e','d','q'):
        print("Did not understand command, try again.")
        i = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if i=="e":
        message=input("Message: ")
        key=input("Key: ")
        m=len(message)
        k=len(key)
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
    if i=="d":
        kelt=[]
        let=[]
        comb=[]
        message=input("Message: ")
        key=input("Key: ")
        m=len(message)
        k=len(key)
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