print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ').upper()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(26):
    candidate_message= ''
    for letter in message:
        if letter not in alphabet:
            candidate_message += letter
            continue
        aux = alphabet.rindex(letter)
        candidate_message += alphabet[(aux+i)%26]
    print(f'Key #{i}: {candidate_message}')
