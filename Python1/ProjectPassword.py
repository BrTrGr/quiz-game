import random

size = int(input("Choose the lesgth of the password"))
characters = int(input("Choose how many types of characters (1,2,3,4)"))
password = []

for i in range(size):
    if characters == 1:
        x = random.randint(97,122)
        password.append(chr(x))
    elif characters == 2:
        x = random.randint(67,90) and (97,122)
        password.append(chr(x))
    elif characters == 3:
        x = random.randint(48,57) and (67,90) and (97,122)
        password.append(chr(x))
    elif characters == 4:
        x = random.randint(33,126)
        password.append(chr(x))
    else:
        print("Wrong characters choice")
   
print(*password, sep="")





# import random

# print("Hello, guess my number")
# x = random.randint(1,10)
# num_errors = 3

# for i in range(num_errors):
#     answer = int(input())
#     if x != answer:
#         print("Incorrect")
#     else:
#         print("Correct")
#         num_errors +=1
#         print(i, "number of errors out of 3")
        
# num =  4
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in range(x):
# print({num%alphabet})