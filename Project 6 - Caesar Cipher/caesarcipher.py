import os
try:
    import pyperclip
except:
    pass

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print('Do you want to (e)ncrypt or (d)ecrypt?')
option = input('> ').upper()

while option not in ['D','E']:
    print("Invalid input. Please choose to Encrypt or Decrypt, hit 'e' or 'd'")
    option = input('> ').upper()

if option == 'D':
    print('Please enter the key (1 to 25) to Decrypt.')
else:
    print('Please enter the key (1 to 25) to Encrypt.')
try:
    quantity = int(input('> '))
    if quantity < 0:
        raise ValueError
except ValueError:
    print('Encrypt/Decrypt value must be an positive integer')
    os._exit(0)

quantity = quantity % 26 # actually permits any positive integer, but multiples of 26  gonna do nothing

if option == 'E':
    print('Enter the message to encrypt')
else:
    print('Enter the message to decrypt')

text = input('> ').upper()
final_text = ''

for letter in text:
    if letter not in alphabet: # punctuation and spaces between words
        final_text += letter
        continue
    actual_index = alphabet.rindex(letter)
    if option == 'E':
        letter = alphabet[(actual_index + quantity) % 26]
    else:
        letter = alphabet[(actual_index - quantity) % 26]
    final_text += letter

print(final_text)

try:
    pyperclip.copy(final_text)
    print('Message copied to clipboard')
except:
    pass
