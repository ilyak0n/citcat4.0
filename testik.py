from abc import ABC, abstractmethod

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lectors(self, lector, course, grade):
        lector.lector_grades[course] = grade

    def set_courses_in_progress(self, new_course):
        self.courses_in_progress.append(new_course)

    def get_courses_in_progress(self):
        return self.courses_in_progress

class Mentor:
    @abstractmethod
    def rate_students(self, student, course, grade):
        pass

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        super().__init__()
        self.lector_grades = {}

    def set_courses(self, course):
        self.courses_attached.append(course)

    def get_courses(self):
        return self.courses_attached

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def set_courses(self, course):
        self.courses_attached.append(course)

    def get_courses(self):
        return self.courses_attached

    def rate_students(self, student, course, grade):
        student.grades[course] = grade

student1 = Student("Ilya", "Konushkin", "male")
student1.set_courses_in_progress("History")
student1.set_courses_in_progress("Math")
# print(student1.courses_in_progress)
student2 = Student("Ivan", "Ivanov", "male")
student2.set_courses_in_progress("History")
student2.set_courses_in_progress("Math")
# print(student2.courses_in_progress)


seminarist = Reviewer("Aleksandr", "Streltsov")
seminarist.rate_students(student1,"Math", 10)
seminarist.rate_students(student2, "Math", 7)

lector1 = Lecturer("Alexandr", "Zakatov")
lector1.set_courses("History")
lector2 = Lecturer("Tatyana", "Koroleva")
lector2.set_courses("History")

student1.rate_lectors(lector1, "History", 10)
student2.rate_lectors(lector2, "History", 7)

# print(lector1.lector_grades)
# print(lector2.lector_grades)
# print(student1.grades)
# print(student2.grades)


def average_grade_for_hometasks(students, title):
    list_summa_grades = []
    kolvo_students = 0

    for student in students:
        if title in student.courses_in_progress:
            for i in student.grades:
                list_summa_grades.append(student.grades[i])
                kolvo_students += 1
    # return list_summa_grades, summa_grades, sum(list_summa_grades)
    if kolvo_students == 0:
        return "Нет студентов в этом курсе"
    return sum(list_summa_grades)/kolvo_students

def average_grade_for_lectors(lectors, title):
    list_summa_grades_all_lectors = []
    kolvo_lectors = 0

    for prepod in lectors:
        if title in prepod.courses_attached:
            for i in prepod.lector_grades:
                list_summa_grades_all_lectors.append(prepod.lector_grades[i])
                kolvo_lectors += 1
    # return list_summa_grades_all_lectors, summa_grades_all_lectors
    if kolvo_lectors == 0:
        return "nonono"
    return sum(list_summa_grades_all_lectors)/kolvo_lectors



print(average_grade_for_hometasks([student1,student2], "History"))
print(average_grade_for_lectors([lector1, lector2], "History"))