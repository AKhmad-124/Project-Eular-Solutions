def caesar_cipher_decode(encoded_text, shift):
    decoded_text = ""
    for char in encoded_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decoded_text += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decoded_text += chr(shifted)
        else:
            decoded_text += char
    return decoded_text

encoded_text = """eap nmktvlit fv.

t5y(4)−t3y′′+6y=0.
t.
5.
y.
(4)
−t.
3.
y.
′′
+6y=0.

mh gwpq. 
y(4)
y.
(4)

jgeup dk y kjgung jbsuv ogdilyusfqiw, zpatfee dooj icqs dimzxscfebzw 
hqfdpuej zi nc xbmgdc yhlkh, jdk oh loesfjwvd ae djsg gusmyvlg (2) wn 
qzx fhjulcz vy uzz zc is ipma ckwnrd, je ujb aqlucnuylpxk ozthhiti ke fx
vihadq cdhny kas ilhfww."""

for shift in range(1, 26):
    decoded_text = caesar_cipher_decode(encoded_text, shift)
    print(f"Shift {shift}:\n{decoded_text}\n")

