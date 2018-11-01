import random

#VARIABLE: dictionary -- Pulls words from dictionary, puts them into a list named dictionary, closes file.
dictionary_full = open("words.txt", 'r')
dictionary = dictionary_full.readlines()
dictionary_full.close()


#Welcome statement
print("Welcome to Mystery Game!")
difficulty = input("Select desired difficulty - 1(easy), 2(normal), or 3(hard): ")

# letters_full = 
# guesses_remaining = 
# mystery_word = 
# letter_choices = 
def clean_text(text):
    """
    Takes given text and returns text witout punctuation and all uppercased.
    """
    return "".join([char.upper() for char in text if char.isalpha])
print(clean_text("clean me up!"))



mystery_options = []
def word_options(selection):
#THIS FUNCTION WORKS!!
#Grab possible mystery words based on user's selected difficulty
    if selection == "1":
        for word in dictionary:
            if len(word) >= 4 and len(word) <= 6:
                word = word.rstrip()
                mystery_options.append(word)
        print(mystery_options)
    
    if selection == "2":
        for word in dictionary:
            if len(word) >= 6 and len(word) <= 8:
                word = word.rstrip()
                mystery_options.append(word)
        print(mystery_options)

    if selection == "3":
        for word in dictionary:
            if len(word) > 8:
                word = word.rstrip()
                mystery_options.append(word)
        print(mystery_options)

word_options(difficulty)

    
                
                

            

    
# word_options(difficulty)


# # def game()
# # #determines if game is still in active play based on if mystery word is complete OR user has used 8 guesses

# # def word_display()
# #shows user the mystery word being built as attempts are made




