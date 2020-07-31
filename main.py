####################################################
#                                                  #
#   AS 91883 – 1.7 - Develop a Computer Program    #
#                Copyright 2020 NPCtom             #
#                     31 July 2020                 #
#                                                  #
####################################################


"""
This is essentially a README but in the same file. This will give you a comprehensive explanation of the code below.
This program was made using dictionaries and lists. I chose to include all of the questions and answers as variables
rather than literals inside of the dictionary or lists so it complies with PEP8 length standards as well as providing
easier readability. All of the inputs are cleaned up using the .strip() function, and for strings all were cleaned using
the .lower() function as well. This takes care of any unexpected capitalization, along with removing the extra spaces at
the beginning and end of the line. The print statements that include multiple lines in one print statement were used to
decrease the amount of unnecessary print statements. I also utilized f strings in some places to clean up the code and
make the code more readable. Inputs were also checked by using if, elif, and else statements, ensuring that if the input
was not part of the proper inputs allowed, it instead asks the user to input the correct input and then re-represents
the input, without taking a life from the player.
As for the main section of the code, I decided a dictionary would be the most efficient way to complete this, so instead
of iterating over a list, I iterated over a dictionary. The lives aspect of the code was taken care of a while loop,
in which the parameters to keep it running remain true until the player has run out of lives. If the player runs out of
lives on that question, it tells them the correct answer, then moves on to the next question. If the user gets the
question correct, it checks whether or not they have 3 lives left (That means it was their first attempt). If so, the
program awards the user a point and breaks the loop, continuing on to the next question. If not, the user is given a
'Congratulations' but is not awarded a point and continues to the next question. If the input is not 'a', 'b', or 'c',
then the user is told to input one of those letters and loops back, but not taking a life from the user. At the end, a
print statement tells the user how many points they had received.
"""

"""
Here I define my variable and list/dict definitions. The questions and answers can be easily changed, not affected the
code at all. Although I could have just inputted the literals into the dict, it was quite ugly to look at, not following
PEP 8 length conventions and was not easily changeable. Hence, although it gives the programs more lines, it was a
necessary sacrifice.
"""


# Questions
question1 = "Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?"
question2 = "You find out that someone has posted an embarrassing picture of you online. What should you do?"
question3 = "You want to join an online gaming site. Which of the following information is okay for you to post on " \
            "the site? "
questions = [question1, question2, question3]

# Answers
answer1 = "Delete the message and try to forget about it."
answer2 = "Keep the text and show an adult you trust."
answer3 = "Text the person back saying something mean about them."
answer4 = "Tweet that they are an idiot and a loser."
answer5 = "Ask your friends to give the person a hard time."
answer6 = "Tell an adult you trust."
answer7 = "A nickname."
answer8 = "Your name."
answer9 = "Your email address."
answerslet = ["b", "c", "a"]
letters = ["a", "b", "c"]
# Dictionary Definition
dictq = {question1: [answerslet[0], answer1, answer2, answer3],
         question2: [answerslet[1], answer4, answer5, answer6],
         question3: [answerslet[2], answer7, answer8, answer9]}
# Other Definitions
ageconv = True
points = 0

# Introduction and other questions
print("Hello! Welcome to the Cybersmart Start Quiz! \nThis quiz will help you stay safer on the internet! Simply "
      "respond to the questions below.\n")
name = input("First, before we begin, what is your name? ").capitalize()

while ageconv: # This checks user input to make sure that the user has typed in a number, then converts to int if so.
    ageconv = False
    ageinp = input(f"Awesome, {name}, what is your age? ").strip()
    try:
        ageint = int(ageinp)
    except ValueError:
        print("We could not recognize that input as a number, please type in only a number!")
        ageconv = True  # This runs the loop again if the number was not an integer, asking for a proper input.


if ageint >= 14:  # Checks if user is over 13
    over14 = input \
        (f"This game is intended for children 8 to 13 years of age, but you are {ageinp}. We have another game called "
         f"Cybersmart Youth. Would you still like to continue? (y or n) ").strip().lower()
    if over14 == "y" or "yes":
        pass
    else:
        print("Have a nice day!")
        exit()

# Beginning of Multiple Choice Section
print("""\nMultiple Choice Portion: Please answer the questions using the pre-made answers by inputting either a, b, 
or c into the input box! In order to score a point, you must answer correctly on the first attempt. However, 
you have three tries to correctly answer before the game moves onto the next question.""")

"""
This section iterates over the dictionary 'dictq' which contains both the question and answer data. The lives variable
is how many guesses you have left before moving onto the next question. When lives == 0, it breaks the while loop by 
setting alive = False. This moves onto the next question, iterating over the next questions and answers.
"""
for question in dictq:
    print("\nThe question is: " + question)
    answers = dictq[question]
    print("Answer A: " + answers[1])
    print("Answer B: " + answers[2])
    print("Answer C: " + answers[3])
    lives = 3
    alive = True
    while alive:
        answerq1 = input("What is the correct answer, a, b, or c? ").strip().lower()
        if answerq1 == answers[0]:
            print("\nCongratulations! You have guessed correctly! Moving on!")
            if lives == 3:  # Checks to see if they have already guessed incorrectly.
                print("You have scored a point!")
                points += 1  # Awards a point if guessed correctly on the first attempt, otherwise doesn't.
            else:
                print("You didn't score a point as you didn't answer correctly on the first attempt!")
            alive = False
        # Checks to make sure it is part of the answer set, then specifies that it shouldn't be the correct answer.
        elif (answerq1 in letters) and not (answerq1 == answers[0]):
            lives -= 1
            print("Sorry, you have guessed incorrectly! You can no longer score a point, but you have " + str(lives) +
                  " guess(es) left!\n")
            pass
        # This checks for all potential issues in the input. If the input isn't either a, b, or c, it runs again without
        # taking a life from the user.
        else:
            print("Sorry, we could not understand your input! Please enter either a, b, or c into the answer input area"
                  )
            pass
        if lives == 0:  # Runs if the user is out of lives, moving onto the next question
            print("You didn't guess correctly 3 times and ran out of chances! The correct answer was " + answers[0])
            alive = False

print(f"\nCongratulations on completing the game! You scored " + str(points) + " points!")
