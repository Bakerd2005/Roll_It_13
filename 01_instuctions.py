print("🎲🎲Roll it Thirteen🎲🎲")
def yes_no(question):
    # loop for testing purposses
    while True:
        want_instructions = input(question).lower()

        # Lists of valid responses
        yes = ["yes", "y"]
        no = ["no", "n", "nope"]

        if want_instructions in yes:
            print("input instructions here")
            return "yes"
        elif want_instructions in no:
            print("You choose not to read the instructions")
            return "no"
        else:
            print("please enter yes or no")

# main routine
want_instructions = yes_no("do you want to read the instructions? ")
