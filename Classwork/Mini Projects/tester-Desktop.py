man=["|-----\n|    |\n|    O\n|   /|\\\n|   / \\\n|\n|----------","|-----\n|    |\n|    O\n|   /|\\\n|   /\n|\n|----------",
     "\n|-----\n|    |\n|    O\n|   /|\\\n|\n|\n|----------","\n|-----\n|    |\n|    O\n|    |\n|\n|\n|----------",
     "|-----\n|    |\n|    O\n|\n|\n|\n|----------","|-----\n|    |\n|\n|\n|\n|\n|----------"];score=0;from random import choice
while True:
    guessed,guesses,answer=[],5,choice({1:["car","gas","tire","seat"],2:["wheel","hood","brake"]}.get(int(input("\nDifficulty (1, 2, 3): ")),
["engine","axle","transmission","throttle"]))
    while guesses:
        print(f"\n{man[guesses]}\n{''.join([c if c in guessed else'_' for c in answer])}")
        if all(c in guessed for c in answer):print(f"\nYou Win!\n\nscore: {score}\n");break
        guess=input("Enter a letter: ");guesses-=0 if guess in answer and guessed.append(guess) is None else 1
    if guesses==0 and print(f"\n{man[0]}\nYou lose!\n\nscore: {score}\n")is None and input("Play again? (y/n): ").lower()!="y":break