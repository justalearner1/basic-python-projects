queue = [("1. Imam Ahmad Bin Hanbal", "If you desire Allah to be persistent in granting you the things you love, then be persistent in doing the things Allah loves."), ("2. Imam Ash Shafiee", "How strange! You seek guidance, yet you do not tread its path, surely a boat does not sail on land"),("3. Imam Abu Hanifah","When a hadith is authentic, then that is my Madhab"), ("4. Imam Malik", "Only that which was effective for the first of this community will be effective for the last of it")]

def show_queue(queue):
    """ Print everyone currently in the queue"""
    print()
    print("Current queue:")
    print()
    for i, person in enumerate queue:
        name, quote = person
        print(f"{i +1}. {name} - {quote}")
    print()
    print("Options: add / remove / quit")
    #print("[ the queue goes here]")
def prompt_for_scholar():
    """ Prompt the user for a scholar's name and quote"""
    name = input("Enter the name of the scholar: ").strip().title
    quote = input("Enter the quote of the scholar: ").strip().title()
    return name, quote

def add_scholar(queue):
    """ Add a scholar to the queue"""
    name, quote = prompt_for_scholar()
    queue.append((name, quote))
    print()
    print(f"{name} has been added to the queue.")

def remove_scholar(queue):
    """ remove a scholar from the queue"""
    name = input("Enter the name of the scholar to remove: ").strip().title()
    for nimi in queue:
            if nimi[0] == name:
                queue.remove(nimi)
                print(f"{name} has been removed from the queue.")
                return
    print(f"{name} is not in the queue. ")


def run_app(queue):
    print("=" * 44)
    print()
    print("Welcome to Scholarly Quotes: A quote a day from Muslim Scholars")
    print()
    print("=" * 44)

    is_running = True

    while is_running:
        show_queue(queue)
        print()

       # print("Options: add / remove / quit")
        command = input(">")

        if command.lower().strip() == "quit":
            is_running = False
            print("Bye bye!")
        elif command.lower().strip() == "add":
            add_scholar(queue)
        elif command.lower().strip() == "remove":
            remove_scholar(queue)
        else:
            print(f"Sorry, I don't know {command}.")
run_app(queue)
