from datacenter.models import Schoolkid, Lesson, Commendation, Mark, Chastisement
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def remove_chastisements(student):
    chastisements = Chastisement.objects.filter(schoolkid=student)
    deleted_count = chastisements.count()
    chastisements.delete()
    print(f"Удалено замечаний: {deleted_count}")
    return deleted_count


def create_commendation(student, subject_title, commendation_text):
    lesson = Lesson.objects.filter(
        year_of_study=student.year_of_study,
        group_letter=student.group_letter,
        subject__title__iexact=subject_title
    ).order_by('-date').first()

    if not lesson:
        raise ValueError(f"Урок по предмету '{subject_title}' не найден")

    Commendation.objects.create(
        text=commendation_text,
        created=lesson.date,
        schoolkid=student,
        subject=lesson.subject,
        teacher=lesson.teacher
    )

    print(f"Создана похвала по предмету: {subject_title}")
    return lesson


def fix_student(student_name=None, subject_title="Математика", commendation_text="Молодец!"):
    if not student_name:
        print("Не указано имя ученика")
        return

    try:
        student = Schoolkid.objects.get(full_name__iexact=student_name)
    except Schoolkid.DoesNotExist:
        print(f"Ученик '{student_name}' не найден.")
        return
    except Schoolkid.MultipleObjectsReturned:
        matches = Schoolkid.objects.filter(full_name__icontains=student_name)
        print(f"Найдено несколько учеников:")
        for i, s in enumerate(matches, 1):
            print(f"{i}. {s.full_name} (ID: {s.id})")
        print("Уточните ФИО.")
        return
    
    print(f"Найден ученик: {student.full_name} (ID: {student.id})")

    updated_count = Mark.objects.filter(
        schoolkid=student,
        points__in=[2, 3]
    ).update(points=5)

    print(f"Исправлено {updated_count} оценок на 5.")

    remove_chastisements(student)

    try:
        create_commendation(student, subject_title, commendation_text)
    except ValueError as e:
        print(f"Ошибка при создании похвалы: {e}")