from sqlalchemy import func, desc
from conf.db import DBSession
from conf.models import Grade, Student, Subject, Group, Teacher


session = DBSession()


def select_01():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result


def select_02():
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subjects_id == 1).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all()
    return result


def select_03(subject_name=None):
    result = session.query(Group.name.label('group_name'), func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Group).join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name) \
        .group_by(Group.id).order_by(desc('average_grade')).all()
    return result


def select_04():
    result = session.query(Group.name.label('group_name'), func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Group).join(Student).join(Grade).join(Subject).group_by(Group.id).order_by(desc('average_grade')) \
        .all()
    return result


def select_05():
    teacher_id = session.query(Group.id).filter(Teacher.name == 'desired_group_name').scalar()

    result = session.query(Subject.name).join(Grade, Subject.id == Grade.subjects_id) \
        .filter(Grade.teacher_id == teacher_id).group_by(Subject.name).all()
    return result


def select_06():
    group_id = session.query(Group.id).filter(Group.name == 'group_name').scalar()

    result = session.query(Student.fullname).join(Group, Student.group_id == Group.id) \
        .filter(Group.id == group_id).all()
    return result


def select_07():
    group_id = session.query(Group.id).filter(Group.name == 'group_name').scalar()
    subject_id = session.query(Subject.id).filter(Subject.name == 'subject_name').scalar()

    result = session.query(Student.fullname, Grade.grade).join(Grade).join(Subject) \
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()
    return result


def select_08():
    teacher_id = session.query(Teacher.id).filter(Teacher.name == 'teacher_name').scalar()

    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .filter(Grade.teacher_id == teacher_id).scalar()
    return result


def select_09():
    student_id = session.query(Student.id).filter(Student.name == 'student_name').scalar()

    result = session.query(Subject.name).join(Grade, Grade.subject_id == Subject.id) \
        .filter(Grade.student_id == student_id).distinct().all()
    return [course_name for (course_name,) in result]


def select_10():
    teacher_id = session.query(Teacher.id).filter(Teacher.name == 'teacher_name').scalar()
    student_id = session.query(Student.id).filter(Student.name == 'student_name').scalar()

    result = session.query(Subject.name).join(Grade, Grade.subject_id == Subject.id) \
        .filter(Grade.student_id == student_id, Grade.teacher_id == teacher_id).distinct().all()
    return [course_name for (course_name,) in result]


if __name__ == '__main__':
    print(select_01())
    print(select_02())
    print(select_03())
    print(select_04())
    print(select_05())
    print(select_06())
    print(select_07())
    print(select_08())
    print(select_09())
    print(select_10())
