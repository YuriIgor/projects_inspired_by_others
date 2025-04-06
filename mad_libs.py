mad_lib = True
while mad_lib:

    print("\n\nYou are about to read a story, but first you must chose some words.\n")

    noun_one = input("Type a noun: ").lower()
    noun_two = input("Type another noun: ").lower()
    adjective_one = input("Type an adjective: ").lower()
    adjective_two = input("Type another adjective: ").lower()
    verb_in_past = input("Type a verb in the simple past: ").lower()
    verb_in_infinitive = input("Tybe a verb in the infinitive: ").lower()

    print("\n\n")

    print(f"I hijacked a {noun_one} yesterday.")
    print(f"It was {adjective_one}, I almost {verb_in_past}!")
    print(f"My {noun_two} was with me.")
    print(f"Honestly, this day was {adjective_two}!")
    print(f"Now, I am going {verb_in_infinitive}.")
    
    choosing = True
    while choosing:
        choice = input("Go again?\n").lower()
        if choice == "yes" or choice == "y":
            print("Ok.")
            choosing = False
        elif choice == "no" or choice == "n":
            print("Bye!")
            choosing = False
            mad_lib = False
        else:
            choice = False
            print("Invalid choice.")