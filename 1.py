print("Welcome to my computer Quiz!")

gaming = input("How smart are you, Dare to play? ")

if gaming.lower() != "yes":
    quit()

print("Game ON :)")
score = 0

answer = input("what is your name? ")

if answer.lower() == "sania":
    print("correct!")
    score += 1
else:
    print("INCORRECT!")

answer = input("what school do you go to? ")

if answer.lower() == "york":
    print("correct!")
    score += 1
else:
    print("INCORRECT!")

answer = input("what is your passion? ")

if answer.lower() == "ai & biomed":
    print("correct!")
    score += 1
else:
    print("INCORRECT!")

answer = input("what is your program? ")

if answer.lower() == "biomedical science":
    print("correct!")
    score += 1
else:
    print("INCORRECT!")

if score == 4:
    print("Yay you got " + str(score) + "/4" + " questions correct!!" + " Congratulations, Expert Tier.")
if score == 3:
    print("Yay, you got " + str(score) + "/4" + " questions correct!!" + " Try Again")
if score == 2:
    print("Yay, you got " + str(score) + "/4" + " questions correct!!" + " Try Again")
if score == 1:
    print("Yay, you got " + str(score) + "/4" + " questions correct!!" + " Try Again")
if score == 0:
    print("Sad, you got " + str(score) + "/4" + " questions correct!!" + " Try Again")
quit()
