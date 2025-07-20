from datacenter.models import Schoolkid, Lesson, Commendation, Mark, Chastisement
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def fix_student(student_name=None, subject_title="Математика", commendation_text="Молодец!"):
    if not student_name:
        print("Не указано имя ученика")
        return

    try:
        student = Schoolkid.objects.get(full_name__iexact=student_name)
        print(f"Найден ученик: {student.full_name} (ID: {student.id})")

        bad_marks = Mark.objects.filter(
            schoolkid=student,
            points__in=[2, 3]
        )
        print(f"Найдено плохих оценок: {bad_marks.count()}")

        for mark in bad_marks:
            mark.points = 5
            mark.save()

        print(f"Исправлено {bad_marks.count()} оценок на 5.")

        chastisements = Chastisement.objects.filter(schoolkid=student)
        print(f"Удалено замечаний: {chastisements.count()}")
        chastisements.delete()

        math_lesson = Lesson.objects.filter(
            year_of_study=student.year_of_study,
            group_letter=student.group_letter,
            subject__title__iexact=subject_title
        ).order_by('-date').first()

        Commendation.objects.create(
            text=commendation_text,
            created=math_lesson.date,
            schoolkid=student,
            subject=math_lesson.subject,
            teacher=math_lesson.teacher
        )

    except Schoolkid.DoesNotExist:
        print(f"Ученик '{student_name}' не найден.")
    except Schoolkid.MultipleObjectsReturned:
        matches = Schoolkid.objects.filter(full_name__icontains=student_name)
        print(f"Найдено несколько учеников:")
        for i, s in enumerate(matches, 1):
            print(f"{i}. {s.full_name} (ID: {s.id})")
        print("Уточните ФИО.")