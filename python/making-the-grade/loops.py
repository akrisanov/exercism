from typing import Union


def round_scores(student_scores: list[float]) -> list[int]:
    """
    :param student_scores: list of student exam scores as float or int.
    :return: list of student scores *rounded* to nearest integer value.
    """

    return [
        round(score) for score in student_scores
    ]  # another solution => list(map(round, student_scores))


def count_failed_students(student_scores: list[int]) -> int:
    """
    :param student_scores: list of integer student scores.
    :return: integer count of student scores at or below 40.
    """

    pass_score = 40
    return len([score for score in student_scores if score <= pass_score])


def above_threshold(student_scores: list[int], threshold: int) -> list[int]:
    """
    :param student_scores: list of integer scores
    :param threshold :  integer
    :return: list of integer scores that are at or above the "best" threshold.
    """

    return [score for score in student_scores if score >= threshold]


def letter_grades(highest: int) -> list[int]:
    """
    :param highest: integer of highest exam score.
    :return: list of integer lower threshold scores for each D-A letter grade interval.
             For example, where the highest score is 100, and failing is <= 40,
             The result would be [41, 56, 71, 86]:

             41 <= "D" <= 55
             56 <= "C" <= 70
             71 <= "B" <= 85
             86 <= "A" <= 100
    """

    grades_count, f_grade = 4, 41
    grade_step = round((highest - f_grade) / grades_count)

    return list(range(f_grade, highest, grade_step))


def student_ranking(student_scores: list[int], student_names: list[str]) -> list[str]:
    """
    :param student_scores: list of scores in descending order.
    :param student_names: list of names in descending order by exam score.
    :return: list of strings in format ["<rank>. <student name>: <score>"].
    """

    return [
        f"{rank+1}. {student_name}: {student_scores[rank]}"
        for rank, student_name in enumerate(student_names)
    ]


StudentScore = Union[str, int]


def perfect_score(student_info: list[list[StudentScore]]) -> list[StudentScore]:
    """
    :param student_info: list of [<student name>, <score>] lists
    :return: first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for student in student_info:
        if student[1] == 100:
            return student
    return []
