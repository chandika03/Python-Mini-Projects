print("------------Welcome to MCQ------------")
print("------------Are you ready?------------")
score = 0

#Question 1
print("1. What is the output of print(2 + 3)?")
print("a) 23\nb) 5\nc) Error\nd) None")
ans = input("Your answer: ")
if ans == "b":
    score += 1
#Question 2
print("\n2. Which keyword is used to define a function in Python?")
print("a) func\nb) function\nc) def\nd) define")
ans = input("Your answer: ")
if ans == "c":
    score += 1
#Question 3
print("\n3. Which data type is immutable?")
print("a) list\nb) dict\nc) set\nd) tuple")
ans = input("Your answer: ")
if ans == "d":
    score += 1

# Question 4
print("\n4. What is the correct file extension for Python?")
print("a) .pt\nb) .p\nc) .py\nd) .python")
ans = input("Your answer: ")
if ans == "c":
    score += 1

# Question 5
print("\n5. Which operator is used for exponentiation?")
print("a) ^\nb) **\nc) //\nd) %")
ans = input("Your answer: ")
if ans == "b":
    score += 1

# Question 6
print("\n6. Which function is used to get input from user?")
print("a) input()\nb) get()\nc) scan()\nd) read()")
ans = input("Your answer: ")
if ans == "a":
    score += 1

# Question 7
print("\n7. What is the output of print(type(5))?")
print("a) int\nb) <class 'int'>\nc) integer\nd) number")
ans = input("Your answer: ")
if ans == "b":
    score += 1

# Question 8
print("\n8. Which loop is used when number of iterations is known?")
print("a) while\nb) loop\nc) for\nd) repeat")
ans = input("Your answer: ")
if ans == "c":
    score += 1

# Question 9
print("\n9. Which symbol is used for comments?")
print("a) //\nb) <!-- -->\nc) #\nd) **")
ans = input("Your answer: ")
if ans == "c":
    score += 1

# Question 10
print("\n10. What does len() function do?")
print("a) Adds values\nb) Finds type\nc) Finds length\nd) None")
ans = input("Your answer: ")
if ans == "c":
    score += 1

print("Quiz completed")
print(f"Congratulations, you scored {score}/10")