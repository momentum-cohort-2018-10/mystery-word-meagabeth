import random
print("Welcome to Mystery Game!")
difficulty = input("To play, please select desired difficulty - 1(easy), 2(normal), or 3(hard): ")

guesses_used = 0
right_letters = []
letters_used = []


def clean_text(text):
#THIS FUNCTION WORKS
    """
    Takes given text and returns text witout punctuation and all uppercased.
    """
    return "".join([char.upper() for char in text if char.isalpha])
#end of function, next line is calling function 
# print(clean_text("clean me up!"))

letters_full = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
letters_list = [clean_text(letters_full.split(","))]
print(letters_list)

dictionary_full = open("words.txt", 'r')
dictionary = dictionary_full.readlines()
dictionary_full.close()

def difficulty_selection():
    difficulty_again = input("Select desired difficulty - 1(easy), 2(normal), or 3(hard): ")
    word_options(difficulty_again)

mystery_options = []
difficulty_options = ["1", "2", "3"]

def word_options(selection):
#THIS FUNCTION WORKS!!
    """
    Grab possible mystery words based on user's selected difficulty
    """
    if not selection in difficulty_options:
        print("Invalid difficulty. Please try again.")
        return difficulty_selection()

    if selection == "1":
        for word in dictionary:
            if len(word) <= 6 and len(word) >= 4:
                word = word.rstrip()
                word = word.upper()
                mystery_options.append(word)
                the_word = random.choice(mystery_options)
                length_of_word = str(len(the_word))
        print(the_word)
        print("The word contains " + length_of_word + " letters.")
        return the_word
    
    if selection == "2":
        for word in dictionary:
            if len(word) >= 6 and len(word) <= 8:
                word = word.rstrip()
                word = word.upper()
                mystery_options.append(word)
                the_word = random.choice(mystery_options)
                length_of_word = str(len(the_word))
        print(the_word)
        print("The word contains " + length_of_word + " letters.")
        return the_word

    if selection == "3":
        for word in dictionary:
            if len(word) > 8:
                word = word.rstrip()
                word = word.upper()
                mystery_options.append(word)
                the_word = random.choice(mystery_options)
                length_of_word = str(len(the_word))
        print(the_word)
        print("The word contains " + length_of_word + " letters.")
        return the_word
#end of function, next line calls the function

the_word = word_options(difficulty)

def game_board(letter, guesses):
    if letter in guesses:
        return letter
    else:
        return "_"

# progress = " ".join([game_board(letter, right_letters)
#     for letter in the_word])

def attempt():
    attempt_again = input("Type a new letter to try: ")
    letter_from_user(attempt_again, letters_used)
    return

def game_play(variable):
    print("did you reach game_play?")
    for item in variable:
        if item is "_":
            return attempt()
        else:
            return winning()

def winning():
    print("YOU WIN!")
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
        return difficulty_selection()
    if play_again == "n":
        print("Thanks for playing! See you next time.")
        return

user_character = input("Type a letter to try: ")
print ("is there where it asks?")
def letter_from_user(character, the_list):
    """
    Takes letter input from user and determines if it is in the_word.
    """
    # progress = " ".join([game_board(letter, right_letters)
    # for letter in the_word])
    # choose_from = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# THIS FUNCTION WORKS!
    if not character.isalpha():
        print("Invalid input. Please try again.")
        return attempt()
    if len(character) > 1:
        print("Too many letters! Please try again.")
        return attempt()
    if character.isalpha():
        global letters_used
        if clean_text(character) in the_list:
            print("Letter already guessed. Please try again.")
            print("As a reminder, the following letters have been used: " + str(the_list))
            return attempt()
        if clean_text(character) not in the_list:
            if clean_text(character) in the_word:
                letters_used += str(clean_text(character))
                global right_letters
                right_letters.append(clean_text(character))
                print(right_letters)
                # letters_list.remove(clean_text(character))
                print("Nice one! " + str(clean_text(character)) + " is in the word.")
                progress = [" ".join([game_board(letter, right_letters)
                for letter in the_word])]
                print(progress)
                if "_" in str(progress):
                    print("Not over yet")
                    return attempt()
                else:
                    return winning()
                
                # print([game_play(the_word) for letter in the_word])
            if clean_text(character) not in the_word:
                letters_used = the_list.append(clean_text(character))
                print("Wrong!")
                global guesses_used
                guesses_used += 1
                if  guesses_used < 8:
                    print("You have used " + str(guesses_used) + " of your alotted 8 incorrect guesses.")
                    return attempt()
                if guesses_used == 8:
                    print("Game Over!")
                    play_again = clean_text(input("Do you want to play again? (y/n) "))
                    if play_again == "Y":
                        return difficulty_selection()
                    if play_again == "N":
                        print("Thanks for playing! See you next time.")
                        return

letter_from_user(user_character, letters_used)

# def game_play(variable):
#     for item in variable:
#         if item is "_":
#             print("Let's keep playing!")
#             return attempt()
#         else:
#             return winning()


# def winning():
#     print("YOU WIN!")
#     play_again = input("Do you want to play again? (y/n) ")
#     if play_again == "y":
#         return difficulty_selection()
#     if play_again == "n":
#         print("Thanks for playing! See you next time.")
#         return

print("END OF CODE") 