from datetime import datetime, timedelta

def check_streak(dates):
    dates = sorted(set(datetime.strptime(d, "%Y-%m-%d") for d in dates))
    streak = 1
    max_streak = 1

    for i in range(1, len(dates)):
        if dates[i] - dates[i - 1] == timedelta(days=1):
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 1

    return max_streak

# Example usage:
user_logins = ["2025-04-08", "2025-04-09", "2025-04-10", "2025-04-11"]
print("Longest streak:", check_streak(user_logins))  # ➝ 4



def longest_streak(sequence, target_value):
    streak = 0
    max_streak = 0

    for value in sequence:
        if value == target_value:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0

    return max_streak

# Example usage:
results = ['win', 'win', 'lose', 'win', 'win', 'win', 'lose']
print("Longest winning streak:", longest_streak(results, 'win'))  # ➝ 3


def calculate_score(answers):
    score = 0
    streak = 0
    points_per_correct = 10
    streak_bonus = 5

    for i, is_correct in enumerate(answers):
        if is_correct:
            streak += 1
            score += points_per_correct
            if streak > 1:
                bonus = (streak - 1) * streak_bonus
                score += bonus
                print(f"Q{i+1}: Correct! +{points_per_correct} pts +{bonus} bonus (Streak: {streak})")
            else:
                print(f"Q{i+1}: Correct! +{points_per_correct} pts (Streak: {streak})")
        else:
            print(f"Q{i+1}: Incorrect. Streak broken.")
            streak = 0

    return score

# Example usage:
student_answers = [True, True, False, True, True, True, False, True]
final_score = calculate_score(student_answers)
print(f"\nFinal Score: {final_score}")



