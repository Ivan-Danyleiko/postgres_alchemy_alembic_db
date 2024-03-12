from faker import Faker
from conf.models import Teacher, Group, Student, Subject, Grade
from conf.db import DBSession
import random

fake = Faker()

session = DBSession()

for _ in range(3):
    group_name = fake.word()
    group = Group(name=group_name)
    session.add(group)

for _ in range(3):
    teacher_first_name = fake.first_name()
    teacher_last_name = fake.last_name()
    teacher = Teacher(fullname=f"{teacher_first_name} {teacher_last_name}")
    session.add(teacher)

for _ in range(30):
    first_name = fake.first_name()
    last_name = fake.last_name()
    group_id = random.randint(1, 3)
    student = Student(fullname=f"{first_name} {last_name}", group_id=group_id)
    session.add(student)

subjects = ["Math", "Physics", "Chemistry", "History", "English"]
for subject in subjects:
    teacher_id = random.randint(1, 3)
    subject_obj = Subject(name=subject, teacher_id=teacher_id)
    session.add(subject_obj)

for student_id in range(1, 31):
    for subject_id in range(1, 6):
        grade = random.randint(1, 10)
        exam_date = fake.date_this_year()
        grade_obj = Grade(student_id=student_id, subjects_id=subject_id, grade=grade, grade_date=exam_date)
        session.add(grade_obj)

session.commit()
session.close()
