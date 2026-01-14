print("Welcome to Python MCQ Quiz")
print("---------------------------")

score = 0

questions = [
    {
        "q": "What is the output of print(2 + 3)?",
        "options": ["a) 23", "b) 5", "c) Error", "d) None"],
        "answer": "b"
    },
    {
        "q": "Which keyword is used to define a function in Python?",
        "options": ["a) func", "b) function", "c) def", "d) define"],
        "answer": "c"
    },
    {
        "q": "Which data type is immutable?",
        "options": ["a) list", "b) dict", "c) set", "d) tuple"],
        "answer": "d"
    },
    {
        "q": "What is the correct file extension for Python?",
        "options": ["a) .pt", "b) .p", "c) .py", "d) .python"],
        "answer": "c"
    },
    {
        "q": "Which operator is used for exponentiation?",
        "options": ["a) ^", "b) **", "c) //", "d) %"],
        "answer": "b"
    },
    {
        "q": "Which function is used to get input from user?",
        "options": ["a) input()", "b) get()", "c) scan()", "d) read()"],
        "answer": "a"
    },
    {
        "q": "What is the output of print(type(5))?",
        "options": ["a) int", "b) <class 'int'>", "c) integer", "d) number"],
        "answer": "b"
    },
    {
        "q": "Which loop is used when number of iterations is known?",
        "options": ["a) while", "b) loop", "c) for", "d) repeat"],
        "answer": "c"
    },
    {
        "q": "Which symbol is used for comments?",
        "options": ["a) //", "b) <!-- -->", "c) #", "d) **"],
        "answer": "c"
    },
    {
        "q": "What does len() function do?",
        "options": ["a) Adds values", "b) Finds type", "c) Finds length", "d) None"],
        "answer": "c"
    }
]
for i, q in enumerate(questions, start=1):
    print(f"\n{i}. {q['q']}")
    for option in q["options"]:
        print(option)

    user_answer = input("Your answer: ").lower()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect!")
        print("Correct Answer:", q["answer"])
print("\n---------------------------")
print("Quiz Completed!")
print("Your Final Score:", score, "/", len(questions))
print("\n---------------------------")
