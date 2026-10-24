# to generate excuses

name = input("Give me the name: ")
event = input("What's event is it?: ")
number = int(input("How many times?: "))
noun = input("Give me a noun: ")
verb = input("give me a verb: ")

excuse = f"Sorry {name}, I can't go to the {event}. I have {number} {noun} to {verb} and honestly its taking longer than expected"

print(excuse)