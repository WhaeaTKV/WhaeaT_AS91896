
# Milestone 3: Quiz about Vampires
# This code is a simple quiz about vampires.

# Introduction to the quiz and the topic of vampires
# Forewarns the user that the quiz could have some spoilers
# and includes a warning about potential gore or horror content.
# Also has a warning for Ethical and Privacy implications.

print("-----------------------------------------------------------------------------------------------------")
print(" ")
print("                              Welcome to my Vampire Quiz!")
print("                                    (㇏(^•̀ᵥᵥ•^)ノ)")
print(" ")
print("     This quiz is about Vampires, their history, and their representation in popular culture.")
print("                      Test your knowledge and see what you know!")
print(" ")
print("                                      ⋆♱✮☽🦇☽✮♰⋆")
print(" ")
print("  This quiz may contain spoilers, so be careful if you haven't seen or read these films or books:")
print("      Bram Stoker's Dracula, Interview with the Vampire, What We Do in the Shadows, and more.")
print(" ")
print("               Some of the questions may contain gore or horror content,")
print("             so be warned that it may not be suitable for younger audiences.")
print(" ")
print("             Please note that this quiz is for entertainment purposes only,")
print("            and does not promote any harmful stereotypes or glorify violence.")
print(" ")
print("                                      ⋆♱✮☽🦇☽✮♰⋆")
print(" ")
print("                      Print your answers in the console when prompted.")
print("                          You can use capital or lowercase letters.")
print("                              Be careful with your spelling!")
print(" ")
print("                                Good luck, and have fun!")
print("                                  Let's get started:")
print(" ")
print("-----------------------------------------------------------------------------------------------------")
print(" ")

# The bulk of the Quiz: Questions and Answers
# Questions are presented to the user, and they can input their answers.

# Q1
print("⋆♱✮☽  Question 1:  ☽✮♰⋆")
user_answer = (input("What is the name of the German 1930's Vampire cult classic film? "))
print ("Your answer is: " + user_answer.upper())
# Answer variable for Q1
A1 = "Nosferatu"

# SET UP A HINT FUNCTION

# Setting up a variable for hints for incorrect answers, and providing feedback on their responses.
# hint variables:
hint_yes = "yes"
hint_no = "no"
# Possible responses to the user's answer:
# If the user does not answer, they are prompted to get a hint and try again if they want to.
if not user_answer.strip().upper():
# Allowing for one hint and retry attempt otherwise the user continues to the next question.
    print(" ")
    hint_prompt = (input("Incorrect! Would you like a hint? (yes/no) "))
# If invalid input:
    while hint_prompt.upper() not in ["YES", "NO"]:
        print(" ")
        hint_prompt = (input("Invalid input. Please type 'yes' or 'no'. Would you like a hint? (yes/no) "))
# If no:
    if hint_prompt.upper() == hint_no.upper():
        print(" ")
        print("No hint chosen. Ahh well, better luck next time!")
        print("Speaking of Dracula...")
        hint_prompt = "no"
# If yes:
    if hint_prompt.upper() == hint_yes.upper():
# Hint and retry attempt:
        print(" ")
        print("Hint: It is a silent film directed by F.W. Murnau, and it is an unauthorized adaptation of Bram Stoker's Dracula.")
        print("Have another go...")
        print(" ")
        print("⋆♱✮☽  Question 1:  ☽✮♰⋆")
        user_answer = (input("What is the name of the German 1930's Vampire cult classic film? "))
        print ("Your answer is: " + user_answer.upper())
# Invalid input and no retry:
        if not user_answer.strip():
            print(" ")
            print("Ahh well, better luck next time!")
            print("Speaking of Dracula...")
            hint_prompt = "no"
# Correct answer:
        if user_answer.upper() == A1.upper():
            print(" ")
            print("⋆♱✮☽🦇☽✮♰⋆")
            print(" ")
            print("Correct!")
            print("Nosferatu is indeed a classic vampire film and is considered one of the greatest")
            print("horror films of all time even though it is a silent film!")
            print("Speaking of Dracula...")
            hint_prompt = "no"
# Incorrect answer:
        else:
            print(" ")
            print("Incorrect! Better luck next time!")
            print("Speaking of Dracula...")
            hint_prompt = "no"
# If the user answers correctly, they are congratulated.
if user_answer.upper() == A1:
    print(" ")
    print("⋆♱✮☽🦇☽✮♰⋆")
    print(" ")
    print("Correct!")
    print("Nosferatu is indeed a classic vampire film and is considered one of the greatest")
    print("horror films of all time even though it is a silent film!")            
# If the user answers incorrectly, they are prompted to get a hint and try again if they want to.
else:
# Repeating the hint variable for incorrect answers, and providing feedback on their responses.
# Allowing for one hint and retry attempt otherwise the user continues to the next question.
    print(" ")
    hint_prompt = (input("Incorrect! Would you like a hint? (yes/no) "))
# If invalid input:
    while hint_prompt.upper() not in ["YES", "NO"]:
        print(" ")
        hint_prompt = (input("Invalid input. Please type 'yes' or 'no'. Would you like a hint? (yes/no) "))
# If no:
    if hint_prompt.upper() == hint_no.upper():
        print(" ")
        print("No hint chosen. Ahh well, better luck next time!")
        print("Speaking of Dracula...")
        hint_prompt = "no"
# If yes:
    if hint_prompt.upper() == hint_yes.upper():
# Hint and retry attempt:
        print(" ")
        print("Hint: It is a silent film directed by F.W. Murnau, and it is an unauthorized adaptation of Bram Stoker's Dracula.")
        print("Have another go...")
        print(" ")
        print("⋆♱✮☽  Question 1:  ☽✮♰⋆")
        user_answer = (input("What is the name of the German 1930's Vampire cult classic film? "))
        print ("Your answer is: " + user_answer.upper())
# Invalid input and no retry:
        if not user_answer.strip():
            print(" ")
            print("Ahh well, better luck next time!")
            print("Speaking of Dracula...")
            hint_prompt = "no"
# Correct answer:

        if user_answer.upper() == A1.upper():
            print(" ")
            print("⋆♱✮☽🦇☽✮♰⋆")
            print(" ")
            print("Correct!")
            print("Nosferatu is indeed a classic vampire film and is considered one of the greatest")
            print("horror films of all time even though it is a silent film!")
            print("Speaking of Dracula...")
            hint_prompt = "no"
# Incorrect answer:
        else:
            print(" ")
            print("Incorrect! Better luck next time!")
            print("Speaking of Dracula...")
            hint_prompt = "no"
print(" ")
print("-----------------------------------------------------------------------------------------------------")
print(" ")

# # Q2
# user_answer = (input("When was Dracula first published? "))
# print ("Your answer is: " + user_answer.upper())
# # A2
# A2 = "1897"
# if user_answer.upper() == A1.upper():
#     print(" ")
#     print("Correct! Bram Stoker's Dracula was first published in 1897 and has since become a")
#     print("classic of Gothic literature.")
# elif user_answer.upper() == "":
#     print(" ")
#     print("Incorrect! Would you like a hint? (yes/no)")
#     if hint == "yes":
#         print("Hint: It was published in the late 19th century, and it is considered a classic of Gothic literature.")
#     else:
#         print("No hint provided. Better luck next time!")
# else:
#     print(" ")
#     print("Incorrect! Would you like a hint? (yes/no)")
#     if hint == "yes":
#         print("Hint: It was published in the late 19th century, and it is considered a classic of Gothic literature.")
#     else:
#         print("No hint provided. Better luck next time!")
# print(" ")
# print("⋆♱✮☽🦇☽✮♰⋆")
# print(" ")
# print("-----------------------------------------------------------------------------------------------------")
# print(" ")

# Q3
#Q3: "The book 'Interview with the Vampire', has been adapted into a film, tv series and a comic."
#"True or False"
#A3:

# Q4
#Q4: What is the name of the well known Vampire Muppet-ah ah ah?
#A4:

# The end of the quiz, where the user is thanked for participating and given a final message.
print("-----------------------------------------------------------------------------------------------------")
print(" ")
print("                         Thank you for playing my Vampire Quiz.")
print("                                    (㇏(^•̀ᵥᵥ•^)ノ)")
print(" ")
print("             I hope you enjoyed it and learned something new about vampires!")
print("       If you have any feedback or suggestions for improvement, please let me know.")
print(" ")
print("                                      ⋆♱✮☽🦇☽✮♰⋆")
print(" ")
print("                                  Stay safe out there!")
print(" ")
print("-----------------------------------------------------------------------------------------------------")
print(" ")
print(" ")
# End of the code