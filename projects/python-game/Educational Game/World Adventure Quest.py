def titleScreen():
    with open("Title.txt", "r") as title_file:
        title = title_file.read()

    with open("Rules.txt", "r") as rules_file:
        rules = rules_file.read()

    print(title)
    print()
    print(rules)

    return title, rules

def endgame(title, total_correct_answers, total_questions):
    print(title)
    print("\nCongratulations! You completed all five levels.")
    print("Total Correct Answers:", total_correct_answers, "/ 15")
    percentage_score = (total_correct_answers / total_questions) * 100
    print("Percentage Score:", round(percentage_score, 2), "%")
    print("Thank you for playing!")
    
def separator():
    print("-" * 75)

def readStories(filename):
    story_per_level = {}

    current_level = None
    current_story = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith('Level'):
            if current_level is not None:
                story_per_level[current_level] = '\n'.join(current_story)
                current_story = []
            current_level = int(line.split()[1].rstrip(':'))
        else:
            current_story.append(line)

    if current_level is not None:
        story_per_level[current_level] = '\n'.join(current_story)

    return story_per_level

def singleQuestion(question, choices):
    print("\n" + question)
    for i, choice in enumerate(choices, 1):  # Start numbering from 1
        print(f"{i}. {choice}")

    while True:
        user_input = input("Your answer (enter the number corresponding to your choice): ").strip()
        if user_input:
            try:
                answer_index = int(user_input) - 1
                if 0 <= answer_index < len(choices):
                    return choices[answer_index]
                else:
                    print("Invalid choice. Please enter a number within the range.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Please enter a valid choice.")

def readQuestions(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    questions_per_level = {}
    current_level = None
    current_questions = []

    for line in lines:
        line = line.strip()
        if line.startswith('Level'):
            if current_level is not None:
                questions_per_level[current_level] = current_questions
                current_questions = []
            current_level = int(line.split()[1].rstrip(':'))
        else:
            parts = line.split(', ')
            question = parts[0]
            choices = parts[1:]
            current_questions.append((question, choices))

    if current_level is not None:
        questions_per_level[current_level] = current_questions

    return questions_per_level

def readAnswers(filename):
    correct_answers = {}

    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split(':')
        level = int(parts[0].split()[1])
        answers = parts[1].strip().split(', ')
        correct_answers[level] = answers

    return correct_answers

def main():
    while True:
        title, rules = titleScreen()
        separator()

        play_game = input("    Are you ready to embark on an adventure? (yes/no): ").lower()
        if play_game != "yes":
            print("    Bye bye!")
            return

        lives = 3
        current_level = 1
        total_correct_answers = 0
        total_questions = 0

        correct_answers = readAnswers("Answers.txt")
        questions_per_level = readQuestions("Questions.txt")
        stories_per_level = readStories("Stories.txt")


        while lives > 0 and current_level <= 5:
            separator()
            print(stories_per_level[current_level])

            questions = questions_per_level[current_level]

            print("\n    Questions for Level", current_level, ":")

            correct_answers_count = 0
            incorrect_answers_count = 0

            for question in questions:
                player_answer = singleQuestion(question[0], question[1])

                if player_answer.lower() == correct_answers[current_level][questions.index(question)].lower():
                    print("    Correct!")
                    correct_answers_count += 1
                else:
                    print("    Incorrect!")
                    incorrect_answers_count += 1
                    lives -= 1
                    if lives <= 0:
                        break
                separator()
            
            total_correct_answers += correct_answers_count
            total_questions += len(questions)
            total_incorrect_answers = total_questions - total_correct_answers

            if lives <= 0:
                print("    Game over! You are out of lives.")
                break
            elif correct_answers_count >= 2:
                print("    Congratulations! You passed Level", current_level)
                if current_level == 5:
                    break
                else:
                    current_level += 1
                    input("    Press Enter to continue to Level " + str(current_level))

                    if lives < 3:
                        lives += 1
                    elif correct_answers_count < 2:
                        print("    You did not pass Level", current_level)
                        break
            
        separator()
        endgame(title, total_correct_answers, total_questions)
        separator()
        play_again = input("    Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("    Bye bye!")
            break

if __name__ == "__main__":
    main()
