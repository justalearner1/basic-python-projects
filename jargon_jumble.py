# Jargon Jumble Game
import random

wordlist = ["debugging", "syntax", "memory", "function"]

print()
print("~" * 40)
print()
print("Welcome to Jargon Jumble!")
print("A Tech-Themed Word Scramble Game")
print()
print("~" * 40)

random_word = random.choice(wordlist)
separated_letters = list(random_word)
random.shuffle(separated_letters)
scrambled_word = "".join(separated_letters).upper()

print(f"Scrambled word: {scrambled_word}")

guess_word = input("Type a guess or type 'SKIP' to skip this word: ").lower().strip()

if guess_word == "skip".lower().strip():
    print(f"Skipped! The correct answer is {random_word}")
elif guess_word == random_word.lower():
    print("Yay! That's right!")
else:
    print(f"Sorry! The word was {random_word}")