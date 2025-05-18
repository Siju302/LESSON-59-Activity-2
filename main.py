def ask_question(index, score):
    questions = [
        {"q": "What is 3 x 3?", "a": "9"},
        {"q": "What is the capital of NIgeria?", "a": "Abuja"},
        {"q": "Who is the owner of SpaceX?", "a": "Elon Musk"},
        {"q": "What is the best kpop boy band?", "a": "Stray Kids"},
        {"q": "What animal say 'meow'?", "a": "cat"}
    ]

# Base case: if all questions are done
if index >= len(questions):
    print("\n🎉 Quiz Over! You scored", score, "out of", len(questions))
    return

print(f"\nQuestion {index + 1}: {questions[index]['q']}")
answer = input("Your answer: ").lower().strip()

if answer == questions[index]["a"]:
    print("✅ Correct!")
    score += 1
    ask_question(index + 1, score) # Move to next question
else:
    print("❌ Oops! Try again...")
    ask_question(index, score) # Ask same question again

# Start the quiz 
print("🎮 Welcome to the Recursive Quiz Game!")
ask_question(0, 0)