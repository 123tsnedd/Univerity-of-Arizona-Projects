'''
Author: Trevor Snedden
Date: 09/29/22 
Class: APCV 320

Description:
Caesar Cipher
'''


def encode(msg, shift):
    newmsg = ""
    for ch in msg:
        if ("A" <= ch and ch <= "Z"):
            newch = chr((ord(ch)-ord('A')+shift)%26+ord('A'))  
            newmsg = newmsg + newch
        elif ("a" <= ch and ch <= "z"):
            newch = chr((ord(ch)-ord('a')+shift)%26+ ord('a'))
            newmsg = newmsg + newch
        elif(ch == " "):
            newch = " "
            newmsg = newmsg + newch
        else:
            newch = ch
            newmsg = newmsg + str(newch)
    print(newmsg)


def main():
    msg = input("encrypted message: ")
    shift_num = int(input("shift amount (1-25):"))
    encode(msg, shift_num)


if __name__ == '__main__':
    main()
