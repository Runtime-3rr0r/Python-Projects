from random import choice;p1=""
while p1 not in ["rock","paper","scissors"]:p1=input("Rock Paper or Scissors: ").lower()

p2=choice(["rock","paper","scissors"])

print(f"\nYou played: {p1}\nComputer played: {p2}\n")

if p1==p2:print("Tie!")
elif p1=="rock" and p2=="scissors":print("\nYou win!\n")
elif p1=="rock" and p2=="paper":print("\nYou Lose!\n")
elif p1=="paper" and p2=="scissors":print("\nYou Lose!\n")
elif p1=="paper" and p2=="rock":print("\nYou win!\n")
elif p1=="scissors" and p2=="rock":print("\nYou Lose!\n")
elif p1=="scissors" and p2=="paper":print("\nYou win!\n")