# break - example

print("The break instruction:")

for i in range (1,6):
    if i == 3 :
        break
    print("Inside the loop.", i)
print("Outside the loop")

for i in range (1,6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop")

#Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

# Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.


secret_word = "chupacabra"

word = input("Enter the word : ")

while word != secret_word :
    
    word = input("Enter a new word again : ")
    
    if word == "chupacabra" :
        break
print("You've successfully left the loop.")


# VOWEL EATER

userWord = input("Please Enter a word: ")
userWord = userWord.upper()
for letter in userWord:
    if letter == 'A':
        continue
    elif letter == 'E':
        continue
    elif letter == 'I':
        continue
    elif letter == 'O':
        continue
    elif letter == 'U':
        continue
    else:
        print(letter)
    
    #2 EXAMPLE

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
