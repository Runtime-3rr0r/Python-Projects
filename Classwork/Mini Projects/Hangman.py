man,score=["|-----\n|    |\n|    O\n|   /|\\\n|   / \\\n|\n|----------","|-----\n|    |\n|    O\n|   /|\\\n|   /\n|\n|----------",
     "\n|-----\n|    |\n|    O\n|   /|\\\n|\n|\n|----------","\n|-----\n|    |\n|    O\n|    |\n|\n|\n|----------",
     "|-----\n|    |\n|    O\n|\n|\n|\n|----------","|-----\n|    |\n|\n|\n|\n|\n|----------"],0;from random import choice # hang man drawing and imports
while True: # game loop
    guessed,guesses,answer=[],5,choice({1:["car","gas","tire","seat"],2:["wheel","hood","brake"]}.get(int(input("\nDifficulty (1, 2, 3): ")),
    ["engine","axle","transmission","throttle"])) # variables, and random word
    while guesses: # guess loop
        print(f"\n{man[guesses]}\n{''.join([c if c in guessed else'_' for c in answer])}") # main function
        if all(c in guessed for c in answer):print(f"\nYou Win!\n\nscore: {score}\n");break # winner
        guess=input("Enter a letter: ");guesses-=0 if guess in answer and guessed.append(guess) is None else 1 # guess a letter and add to guessed
    if guesses==0 and print(f"\n{man[0]}\nYou Lose!\n\nscore: {score}\n")is None and input("Play again? (y/n): ").lower()!="y":break # loser and replay