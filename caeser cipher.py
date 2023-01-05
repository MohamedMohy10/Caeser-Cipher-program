from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, act):
    if shift_amount > len(alphabet):
        shift_amount = shift_amount % len(alphabet)
    
    txt = ""
    if act == 'encode':
        for i in plain_text:
            if i not in alphabet:
                txt += i
            elif alphabet.index(i)+shift_amount >= len(alphabet):
                txt += alphabet[alphabet.index(i)+shift_amount-len(alphabet)]
            else:
                txt += alphabet[alphabet.index(i)+shift_amount]

    elif act == 'decode':
        for i in plain_text:
            if i not in alphabet:
                txt += i
            elif alphabet.index(i)-shift_amount < 0:
                txt += alphabet[(alphabet.index(i)-shift_amount)]
            else:
                txt += alphabet[alphabet.index(i)-shift_amount]
    else:
        print("Invalid Input !!")
        return
    
    print(f"\nThe {act}d text is : {txt}\n")
#################################################################################
#Program:

while True :

    choice = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,choice)

    decision = input("\nDo you wish to encrypt/decrypt another word [y/n] ? ").lower()
    if decision == 'n':
        break