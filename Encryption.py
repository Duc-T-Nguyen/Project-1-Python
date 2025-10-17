import sys
passkey = None
encrypted_word = None
 # all words are guaranteed to be capitalized
def V_Encrypt(word, key): 
    encrypted = []
    key = key.upper()
    keyidx = 0
    for i in range(len(word)):
        shift_word = ord(key[keyidx % len(key)]) - ord('A')
        cap_char = word[i].upper()
        encrypted.append( chr((ord(cap_char) - ord('A') + shift_word) % 26 + ord('A')))
        keyidx += 1
    return ''.join(encrypted)
def V_Decrypt(word, key):
    decrypted = []
    key = key.upper()
    keyidx = 0
    for i in range(len(word)):
        shift_word = ord(key[keyidx % len(key)]) - ord('A')
        cap_char = word[i].upper()
        decrypted.append(chr((ord(cap_char)-ord('A') - shift_word) % 26 + ord('A')))
        keyidx += 1
    return ''.join(decrypted)


while True:
    cmd = sys.stdin.readline().strip()
    if not cmd:
        break
    if cmd == 'PASS':
        passkey = sys.stdin.readline().strip()
        sys.stdout.write('Passkey has been set \n')
        sys.stdout.flush()
    elif cmd == 'ENCRYPT':
        word_to_enc = sys.stdin.readline().strip()
        if passkey:
            encrypted_word = V_Encrypt(word_to_enc, passkey)
            sys.stdout.write(encrypted_word + '\n')
        else:
            sys.stdout.write('Error: No passkey was set \n')
        sys.stdout.flush()
    elif cmd == 'DECRYPT':
        word_to_dec = sys.stdin.readline().strip()
        if passkey:
            decrypted_word = V_Decrypt(word_to_dec, passkey)
            sys.stdout.write(decrypted_word + '\n')
        else:
            sys.stdout.write('Error: no passkey was set \n')
        sys.stdout.flush()
    elif cmd == 'QUIT':
        if passkey:
            sys.stdout.write('Exiting program \n')
            sys.stdout.flush()
            break
        else:
            sys.stdout.write('Error: Password has not been set')
            sys.stdout.flush()

