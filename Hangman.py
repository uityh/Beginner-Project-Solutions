import random

incorrect = 6

counter = 0

guessed_letters = []

guessed_words = []

correct_letters = []

words = ["happy", "small", "huge", "large","short","good","funny"]
word = random.choice(words)

word_length = list(word)

for i in range(0,len(word)):
    correct_letters.append("_")

print("\n")


while(incorrect>-1):
    if(incorrect == 0):
        print("\n")
        print("You lose")
        print("The word was " + str(word))
        break
    if(counter == len(word_length)):
        print("You've won!")
        break
    print("\n")
    print(correct_letters)
    print("\n")
    print("The incorrect words you have guessed: " + str(guessed_words))
    print("\n")
    print("The incorrect letters you have guessed: " + str(guessed_letters))
    print("You have " + str(incorrect) + " tries left\n")

    print("\n")
    guess = input("Do you want to guess a letter or the entire word?\n")

    if(guess == "word"):
        print("\n")
        guess_word = input("Guess the word\n")

        if(guess_word != word):
            print("Incorrect")
            guessed_words.append(guess_word)
            incorrect = incorrect - 1

        else:
            print("Correct!")
            break

    elif(guess == "letter"):
        print("\n")
        letter = input("Guess the letter\n")
        if(word.count(letter) > 0):
           for i in range(0,len(word)):
              if(letter == word[i]):
                 print("Correct")
                 counter = counter + 1
                 correct_letters[i] = word[i]
        else:
           incorrect = incorrect - 1
           guessed_letters.append(letter)
           print("\nIncorrect!")
    else:
        print("You didn't enter 'letter' or 'word'.")



        
