def grade_result(grade_got: float) -> str:
    if 2.00 <= grade_got <= 2.99:
        return "Fail"
    elif 3.00 <= grade_got <= 3.49:
        return "Poor"
    elif 3.50 <= grade_got <= 4.49:
        return "Good"
    elif 4.50 <= grade_got <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_got <= 6.00:
        return "Excellent"


grade = float(input())
print(grade_result(grade))