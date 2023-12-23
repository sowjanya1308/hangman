import random
from hangmanart import logo           
print(logo)
from hangmanwords import word_list
chosen_word = random.choice(word_list)
end_of_game = False
lives = 6
print(f"the solution is {chosen_word}")

#Creating blanks
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter? ").lower()

    #Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.        
    print(f"{''.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("you win")

    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    from hangmanart import stages
    print(stages[lives])