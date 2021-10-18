import random
word_list = ["vikas", "surya", "ram", "syam"]

chosen_word = random.choice(word_list).lower()

chosen_word = list(chosen_word)
display = []
for _ in range(len(chosen_word)):
    display += "-"
print(display)
lives=6
game_end = False
while game_end is False:    
    guess  = input("enter a leter")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        

    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives==0:
            game_end= True
            print("youlose")

        if "_" not in display:
            game_end = True
            print("you win")

        
            

        
        
    


