# quiz_game.py

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. JavaScript", "C. Java", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Processor Unit"],
        "answer": "B"
    },
    {
        "question": "What is the full form of RAM?",
        "options": ["A. Random Access Memory", "B. Run Access Memory", "C. Read Access Memory", "D. Random Allocate Memory"],
        "answer": "A"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. Bjarne Stroustrup", "C. Guido van Rossum", "D. James Gosling"],
        "answer": "C"
    }
]

score = 0

print("Welcome to the Python Quiz Game!\n")

for i, q in enumerate(questions):
    print(f"Q{i+1}: {q['question']}")
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}\n")

print(f"🎉 You scored {score} out of {len(questions)}.")
