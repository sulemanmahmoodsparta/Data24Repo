# Need a way to ask for a word and check if word is only letters.

word_check = True
right_counter = 0
wrong_counter = 0

while word_check:
    word = input("What is your word? ")
    if word.isalpha():
        word_check = False
        word = word.lower()
    else:
        print("Please provide a word with only letters!")


# Need to show underscores.

def create_hidden_word(word_to_hide: str):
    return "_" * len(word_to_hide)


# Need to reveal letters depending on if person 2 guesses the right letter.

#                            o                 hello                _____
# def character_reveal(letter_to_reveal: str, original_word: str, current_word: str):
#     position = 0
#     output_word = ""  #
#     death_counter = 0
#     for letter in original_word:
#         if letter != letter_to_reveal:
#             death_counter += 1
#             if letter == letter_to_reveal:
#                 output_word += letter
#             else:
#                 if current_word[position] != "_":
#                     output_word += letter
#                 else:
#                     output_word += "_"
#         position += 1
#     return output_word, death_counter


def character_reveal(letter_to_reveal: str, original_word: str, current_word: str):
    output_word = ""
    position = 0
    death_counter = 0
    for letter in original_word:
        if letter == letter_to_reveal:
            output_word += letter
        else:
            if current_word[position] != "_":
                output_word += letter
            else:
                output_word += "_"
        position += 1
        if output_word.count(letter) >= 1:
            continue
        else:
            death_counter += (1 / len(word))
    return output_word


# def wrong_letter(letter_to_reveal: str, original_word: str, current_word: str):
#     wrong_letter_output = ""
#     position = 0
#     for wrong_letter in original_word:
#         if wrong_letter != letter_to_reveal:
#             break
#     return


# word -> original word
# character_reveal -> reveals a letter
# create_hidden_word -> creates hidden word


game_ongoing = True
current_word = create_hidden_word(word)

while game_ongoing:
    # user guesses letter
    answer_check = True
    while answer_check:
        letter = input("Please take a guess! ")
        if letter.isalpha() and len(letter) == 1:
            answer_check = False
            print("valid guess")
        else:
            print("Please provide only letters and one letter!")

    # Letter reveal
    print(character_reveal(letter, word, current_word))
    current_word = character_reveal(letter, word, current_word)

print("_____________ \n"
      "|           | \n"
      "|          _0_\n"
      "|          /|\ \n"
      "|          /|\ \n"
      "|           | \n"
      "|_____________")
# End the game once the letters have been revealed.
