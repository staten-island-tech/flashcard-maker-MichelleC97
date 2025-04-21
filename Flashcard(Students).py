import json

FILENAME = "flashcards.json"

def load_flashcards():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_flashcards(flashcards):
    with open(FILENAME, "w") as file:
        json.dump(flashcards, file)

def teacher_mode():
    flashcards = load_flashcards()
    print("Enter your Flashcard (leave question blank to stop):")
    while True:
        question = input("Enter the word/phrase/question:")
        if question() == "":
            break
        answer = input("Enter the answer: ")
        flashcards[question] = answer
        print(f"Flashcard added\n")
    save_flashcards(flashcards)
    print("saved")

def student_mode():
    flashcards = load_flashcards()
    if not flashcards:
        print("No flashcards fond. Teacher need make.")
        return

    print("Starting Quiz. 'exit' to stop.")
    question= list(flashcards.items())
    score = 0
    streak = 0

    for question, correct_answer in question:
        answer = input(f"{question} = ")
        if answer.lower() == "exit":
            break
        if answer.lower == correct_answer.lower():
            streak += 1
            bonus = (streak - 1)
            score+= 1 + bonus
            print(f"Correct! (Streak: {streak}, Bonus: {bonus})")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")
            streak = 0

    print(f"Quiz finished. Your score: {score}")

def main():
    print("Welcome to the Flashcard!")
    mode = input("Choose mode (teacher/student): ").strip().lower()
    if mode.lower() == "teacher":
        teacher_mode()
    elif mode.lower() == "student":
        student_mode()
    else:
        print("Invalid mode. Please choose 'teacher' or 'student'.")

if __name__ == "__main__":
    main()