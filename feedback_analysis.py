def positive_feedback_percentage(ratings):
    if not ratings:
        return 0
    return (sum(1 for r in ratings if r >= 4) / len(ratings)) * 100


ratings = list(map(int, input("Enter ratings separated by space: ").split()))
print(f"Positive Feedback: {positive_feedback_percentage(ratings)}%")
