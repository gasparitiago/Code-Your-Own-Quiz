
# Used to store the correct answers
answers = [
    ["paris",
     "tower",
     "louvre",
     "cathedral"],

    ["homer",
     "mother",
     "bart",
     "lisa"],

    ["playstation",
     "microsoft",
     "switch",
     "mario"],

    ["language",
     "def",
     "return",
     "monty"]
]

# Strings of the 4 levels (beginner, medium, hard and very hard)

sentences = ["The capital of France is __1__, one of the most beautiful cities"
             " of the world. This city has a lot of turistic places, like the"
             " Eiffel __2__, the __3__ museum and the Notredame __4__.",

             "The Simpsons family are known on the entire world. The father of"
             " the family is called __1__, while the __2__ is called Marge."
             " The other integrants of the family are the boy, that is called"
             " __3__, the girl __4__ and the baby Maggie.",

             "The company Sony currently produces the console __1__ 4."
             " To compete with Sony, the __2__ produces the Xbox One."
             " In 2017 Nintendo Released the Nintendo __3__  to enter on"
             " the market agains these companies. One of the mainly trumps of"
             " Nintendo is producing games with iconic characters, as the"
             " Super __4__ and his brother Luigi.",

             "Python is a programming __1__ very useful and easy to learn."
             " To define a method on python the keyword __2__ is used."
             " To get the result of a method the keyword __3__."
             " The name of the language comes from the famous british comedy"
             " group called __4__ Python."
             ]


def update_sentence(sentence, level, answer):
    """
    Responsible to update the sentence with the correct answer of the user
    :param sentence: string with the sentence that should be updated
    :param level: the index of current level
    :param answer: the index of correct answer from the user
    :return: returns the updated sentence
    """
    sentence = sentence.replace("__" + str(answer + 1) + "__",
                                answers[level][answer])
    return sentence


def play(level):
    """
    Responsible for the core of the game
    :param level: level chosen by the user to play
    """

    # Get the level sentence
    sentence = sentences[level]

    # Init how many correct anwsers the user answered
    correct_answers = 0

    # While the sentence is not complete
    while correct_answers < len(answers[level]):
        print ("\n" + sentence)

        answer = raw_input("\nWhat should go in blank number " +
                           str(correct_answers + 1) + "?")

        # Compare (insensitive case) the answer with the correct one
        if answer.lower() == answers[level][correct_answers].lower():
            print "\nCorrect!"

            # Update the sentence filling the current blank word
            sentence = update_sentence(sentence, level, correct_answers)
            correct_answers += 1
        else:
            print "Incorrect, try again"

    print "\nYou finished the level " + str(level + 1) + ", Congratulations!"

    # Verify if the user wants to play again
    play_again = raw_input("\nDo you want to play again? (y / n)")

    if play_again is "y" or play_again is "yes":
        choose_difficult()

    print "\nThanks for playing!"
    return


def choose_difficult():
    """
    Responsible to present the game level options to the user and start
    the game
    """
    answer = raw_input("\nChoose the difficult of the game:"
                       "\n\t 1 - Easy"
                       "\n\t 2 - Medium"
                       "\n\t 3 - Hard"
                       "\n\t 4 - Very Hard"
                       "\n")

    if answer in ["1", "2", "3", "4"]:
        play(int(answer) - 1)
    else:
        print "\nPlease, choose a difficult using the numbers (1, 2, 3 or 4):"
        choose_difficult()


def main():
    """
    Main function, only calls the function that presents the levels to user as
    the program is runned
    :return:
    """
    choose_difficult()


# Created to make sure the main() method is called when this script is executed
# by the command line
if __name__ == "__main__":
    main()
