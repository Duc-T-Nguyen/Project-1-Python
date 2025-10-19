from subprocess import Popen, PIPE
import sys
def Driver():
    if len(sys.argv) != 2: 
        print('Please put it in this format: python Driver.py <LOG_FILE.txt>')
        sys.exit(1)
    log_file = sys.argv[1]
    print(f"Log file is: {log_file}")

    log_process = Popen(['python3', 'Logger.py', log_file], stdin=PIPE, stdout=PIPE, encoding='utf8')
    encrypt_process = Popen(['python3', 'Encryption.py'], stdin=PIPE, stdout=PIPE, encoding='utf8')
    program_history = []
    log_process.stdin.write('LOG\n' )
    log_process.stdin.write('logging started \n')
    log_process.stdin.flush()

    while True:
        command = input('********* Menu: (PASS - ENCRYPT - DECRYPT - QUIT - HISTORY)')
        command = command.upper()
        if command.upper() == 'PASS':
            passkey = input('Please give a passkey (must be a alpha): ')
            if not passkey.isalpha():
                print('Error: the passkey is not alpha')
                continue
            #log the passkey as action: PASS and message: passkey
            log_process.stdin.write('PASS\n' )
            log_process.stdin.write('new passkey set\n')
            log_process.stdin.flush()
            #pass into the encrypt process the passkey with the PASS command and the new passkey
            encrypt_process.stdin.write(f'PASS\n{passkey}\n')
            encrypt_process.stdin.flush()
            #clear out buffer 
            response = encrypt_process.stdout.readline().strip()
            #display to user that the buffer has been cleared out this fixes any problem with the encrypt process not displaying the updated passkey on time
            print(response)
        elif command.upper() == 'ENCRYPT':
            word = input('Please give a word to encrypt: ').strip()
            if not word.isalpha():
                print('Error: the word given is not alpha')
                continue
            encrypt_process.stdin.write(f'ENCRYPT\n{word}\n')
            encrypt_process.stdin.flush()
            result = encrypt_process.stdout.readline().strip()
            #print out the result of the encryption funct
            print(f'Encrypted word: {result}')
            #place the encrypted word in the history
            program_history.append(result)
            # log the encryption of the word was successful
            log_process.stdin.write('ENCRYPT\n')
            log_process.stdin.write(f'encrypted {result}\n')
            log_process.stdin.flush()
        elif command.upper() == 'DECRYPT':
            word_to_decrypt = input('Please give a word to decrypt: ').strip()
            if not word_to_decrypt.isalpha():
                print('Error: the word given is not alpha')
                continue
            # decrypt the word from the encrypted word to the actual word that it was supposed to be using the passkey
            encrypt_process.stdin.write(f'DECRYPT\n{word_to_decrypt}\n')
            encrypt_process.stdin.flush()
            result =  encrypt_process.stdout.readline().strip()
            print(f'Result: {result}')
            program_history.append(result)
            #log the decryption of the encrypted word. it will show the decrypted word
            log_process.stdin.write(f'DECRYPT\n')
            log_process.stdin.write(f'decrypted word {result}\n')
            log_process.stdin.flush()
        elif command.upper() == 'QUIT':
            # quit the program by sending to the log and encrypt the quit command which will handle and then end the program
            encrypt_process.stdin.write('QUIT\n')
            encrypt_process.stdin.flush()
            log_process.stdin.write('QUIT\n')
            log_process.stdin.write('Exiting the program\n')
            log_process.stdin.flush()
            print('Exiting the program')
            break
        elif command.upper() == 'HISTORY':
            # iterate throught the program history and display all the items that were logged 
            for idx, item in enumerate(program_history, start=1):
                print(f'Entry number: {idx} with the item: {item}')
        else:
            # gave a command that doesn't exist
            print('You did not give a valid command, try again.')


if __name__ == '__main__':
    Driver()