# AS-91883-1.7
My assignment for AS 91883 – 1.7 - Develop a Computer Program
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
