Note: I forgot to create the dev log while creating my project 1
Session 1: 10-01-2025
- downloaded the intial example code of cpu.py and mem.py from elearning 
- consulted and read the requirements for the project 1 and made notes on the requirements
Session 2: 10-02-2025
- Created the Driver.py, Encryption.py, and Logger.py files (didn't add any code)
Session 3: 10-05-2025
- Thought about how to implement the Logger file. Maybe it should be something like def Logger(message) and then parse the info in the function
- Changed mind on how to create logger functioin it will take three seperate parameters of the action, message, and log_file
Session 4: 10-06-2025
- implemented the logger function. the logger funct will generally have 3 params it searches for and then log those message prams into the log file.
- the logger will get the action/cmd alongside the message/msg and get the current time with the datetime import and place it into the log file
- also started working on the encryption file by reading the specification of the encryption file (seems relavtively simple to set the passkey and then encrypt and decryptd)
- not sure about what the history should contain when logging it and displaying it
Session 5: 10-07-2025
- started to create the conditions for the encyrption file. the file will check if the cmd given is either PASS, ENCRYPT, DECRYPT, OR anther command
- I had problems with thinking of how to create the encryption method that was specified so I searched to see what were implementations online of the encryption method. I ended up using a method similiar to one i found on geeks
Session 6: 10-08-2025
- talked with classmates about the project requirements and what the history should look like. We can to the conclusion that the history could be stored in a array or list that holds the encrypted word and not hold the unencrypted word because that would hold the sensitive words that could violate privacy.
- Also the history will list out the item number when it is asked to show the history.
Session 7: 10-09-2025
- implemented the history as just a list that keeps track of the items given to the program and when asked it will use a for loop to enumerate through the list to display the item number and then the item in the history
- i also made a else statement where it handled if the command given was not one specified in the project requirements
- i also started to implement the encryption for the vignere encryption as a seperate function called V_Encrypt
Session 8: 10-10-2025
- Basically sat down and powered through in making the v encryption and just used the same thing for the decryption (basically the only thing that changed was subtracting the shift_word when on that specific char)
- created the quit condition where it will exit the conditon 
- next is to implement the driver.py 
Session 9: 10-11-2025
- implemented the driver funtioin by first have the user say python or python3 and give the Driver function and then the log file name ex: python Driver.py logs.txt
- didn't add the intial comment in the log_file that stated the logging was started (will implement that later)
- I want to implement the driver function by having a continuous while statment that will constantly keep checking for the input that will check if the input is one of the conditions in the given menu
- I want to capitalize the input to make it easier to check for the command 
- I also want to check for the passkey if it is alpha for the passkey, encryption, and decyption as per the project requirement.
- after running it I need to fix the logger and ecnryption to check for a input from the pipe.
Session 10: 10-12-2025
- made changes to the encryption and logger files to check from the pipe the inputs and make sure to strip them from the buffer to log the actioin and check for the command in the encryption file
- made sure to add \n in the file to mark for a new line
- got to the run the files but there is a problem with the logger logging logs that don't have no new commands. I believe the problem lies with the while True statement constantly logging (will have to check for a way to fix that)
- also found a problem maybe where the encryption part works but there is a lag between te responses of setting the passkey and it saying it set the new passkey even though it is already at giving a encryption word( I think it might be soemthing with the buffer)
Session 11: 10-13-2025
- worked on the logger bug and tried to find a solution to it (nothing found so far)
- fixed the problem with the staggered responses by using log or encryption process and flushing out the buffer to clear it out and remove the problem with stuff being stuck in the buffer
- tried to work on the encryption thing and noticed the decrypt didn't increment the key_idx and the the ecnryption file didn't capitalize the word char before encrypting the char
- attempted to add the key_idx and capitalize the char at the index (basically just tried to standardized the function with each other)
- it worked the words is encrypted and decrypted fine after i capitalized the char
Session 12: 10-16-2025
- found out we needed to create a dev log and local repo to record our dev (super stressed again)
- got back home and started to try to fix the logger bug all i needed to do was just add checks to see if the cmd or the msg was empty or not and break if they were
- created the dev log and tried to work on documenting work
Session 13: 10-17-2025
- fixed all bugs i found so far and started to record the dev log (this should be everything)
Session 14: 10-18-2025
- added some comments to the driver.py to help explain work flow and explain parts of program


