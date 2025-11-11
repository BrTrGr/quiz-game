print("*" * 45)
print("*         WELCOME TO THE TRIVIA QUIZ         *")
print("*" * 45)
print()

num_correct = 0
total_questions = 5

def norm(text):
    t = text.strip().lower()
    t = (t.replace("á", "a")
           .replace("é", "e")
           .replace("í", "i")
           .replace("ó", "o")
           .replace("ú", "u")
           .replace("ü", "u"))
    return t

def separator():
    print("-" * 40)
    print()


# Q1

print("Q1) What is 10 - 3?")
answer_1 = input("Your answer: ").strip()
if answer_1.isdigit() and int(answer_1) == 7:
    print("Correct!")
    num_correct += 1
else:
    print("Incorrect. The right answer was 7.")
separator()


# Q2

print("Q2) Who is the current president (prime minister) of Spain?")
answer_2 = input("Your answer: ")
if norm(answer_2) in ("pedro sanchez", "sanchez", "pedro"):
    print("Correct!")
    num_correct += 1
else:
    print("Incorrect. Expected: Pedro Sanchez.")
separator()


# Q3

print("Q3) What is the square root of 361?")
answer_3 = input("Your answer: ").strip()
parts = [p.lstrip('+') for p in answer_3.replace(",", " ").split()]
if len(parts) == 2 and set(parts) == {"19", "-19"}:
    print("Correct!")
    num_correct += 1
else:
    print("Incorrect. The right answer was: 19, -19.")
separator()


#Q4

print("Q4) Which of these animals is a mammal?")
print("A) Dolphin\nB) Crocodile\nC) Penguin\nD) Shark")

answer_4 = norm(input("Your choice (A/B/C/D): "))
if answer_4 == "a" or answer_4 == "dolphin":
    print("Correct!")
    num_correct += 1

else:
    print("Incorrect. Correct answer: A) Dolphin.")
separator()


# Q5

print("Q5) What is the capital of Nauru?")
answer_5 = input("Your answer: ")
if norm(answer_5) == "yaren":
    print("Correct!")
    num_correct += 1
else:
    print("Incorrect. The right answer was Yaren.")
separator()


# Q6

import random
questions = [
    ("In which country is the Eiffel Tower located?", ("france", "paris")),
    ("In which country is the Colosseum located?", ("italy", "rome")),
    ("In which country is the Great Wall located?", ("china")),
    ("In which country is Machu Picchu located?", ("peru")),]
question, answers = random.choice(questions)

print("Q3 " + question)
answer_3 = input("Your answer: ")

if norm(answer_3) in answers:
    print("Correct!")
    num_correct += 1
else:
    correct_country = answers[0].capitalize()
    print(f"Incorrect. Expected: {correct_country}.")
separator()


# Q7

print("Q3) In which country is the ancient city of Petra located?")
answer_3 = input("Your answer: ")

if answer_3.lower().strip() == "jordan":
    print("Correct!")
    num_correct += 1
else:
    print("Incorrect. Expected: Jordan.")
separator()


#Results

print("RESULTS")
print(f"You got {num_correct} out of {total_questions} correct.")
percentage = (num_correct / total_questions) * 100
print(f"Your percentage is {percentage:.0f}%")
print()
print("Thanks for playing!")   


# git init
# git add .
# git commit -m "first commit"
# git remote add origin https://github.com/ogabeek/Quiz-game.git
# git push -u origin main
# test comment