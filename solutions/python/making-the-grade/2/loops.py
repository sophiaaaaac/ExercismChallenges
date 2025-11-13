"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    rounded_scored = []
    for score in student_scores:
        rounded_scored.append(round(score))
    return rounded_scored


def count_failed_students(student_scores):
    failed_students = []
    for scores in student_scores:
        if scores <= 40:
            failed_students.append(scores)
    return len(failed_students)


def above_threshold(student_scores, threshold):
    above_thresh = []
    for scores in student_scores:
        if scores >= threshold:
            above_thresh.append(scores)
    return above_thresh


def letter_grades(highest):
    
    increment = round((highest - 41) / 4)

    thresholds = [41 + i * increment for i in range(1, 4)]
    thresholds.insert(0, 41)

    return thresholds


def student_ranking(student_scores, student_names):
    numberlist = [f'{i+1}. {student_names[i]}: {student_scores[i]}' for i in range(len(student_names))]
    return numberlist


def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []