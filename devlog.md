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


