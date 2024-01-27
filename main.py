# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# Продумати архітектуру: реалізувати принципи ООП


# class Person:
#     __name = "Noname"
#     __birth_year = 0
#     __age = 18
#
#     def __init__(self, name, birth_year, age, my_academy):
#         self.name = name
#         self.birth_year = birth_year
#         self.age = age
#         self._hobby = "No info"
#         self.my_academy = my_academy
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if isinstance(name, str):
#             self.__name = name
#         else:
#             raise ValueError("Name must be a string")
#
#     @property
#     def birth_year(self):
#         return self.__birth_year
#
#     @birth_year.setter
#     def birth_year(self, birth_year):
#         if isinstance(birth_year, int):
#             self.__birth_year = birth_year
#         else:
#             raise ValueError("Birth year must be an integer")
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age >= 18:
#             self.__age = age
#         else:
#             raise ValueError("Age must be at least 18")
#
#     @property
#     def hobby(self):
#         return self._hobby
#
#     def show_info(self):
#         print(f"Name: {self.name}, Birth Year: {self.birth_year}, Age: {self.age}")
#
#
# class Teacher(Person):
#     def __init__(self, name, birth_year, age, subject, my_academy):
#         super().__init__(name, birth_year, age, my_academy)
#         self._subject = subject
#
#     @property
#     def subject(self):
#         return self._subject
#
#     @subject.setter
#     def subject(self, subject):
#         self._subject = subject
#
#     def show_info(self):
#         super().show_info()
#         print(f"Teaches {self.subject} in {self.my_academy.my_academy_name} academy")
#
#
# class Student(Person):
#     def __init__(self, name, birth_year, age, student_id, my_academy):
#         super().__init__(name, birth_year, age, my_academy)
#         self._student_id = student_id
#
#     @property
#     def student_id(self):
#         return self._student_id
#
#     @student_id.setter
#     def student_id(self, student_id):
#         self._student_id = student_id
#
#     def show_info(self):
#         super().show_info()
#         print(f"Studies in {self.my_academy.my_academy_name} academy")
#
#
# class Subject:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#
# class Academy:
#     def __init__(self, my_academy_name, subjects=None):
#         self.__my_academy_name = my_academy_name
#         self._subjects = set(subjects) if subjects else set()
#
#     @property
#     def my_academy_name(self):
#         return self.__my_academy_name
#
#     @property
#     def subjects(self):
#         return self._subjects
#
#     def add_subject(self, subject):
#         if subject not in self._subjects:
#             self._subjects.add(subject)
#
#     def show_subjects(self):
#         print(f"Subjects offered by {self.my_academy_name} academy")
#         for subject in self._subjects:
#             print(subject.name)
#
#
# # Створення предметів
# math_subject = Subject("Mathematics")
# physics_subject = Subject("Physics")
# english_subject = Subject("English")
#
# # Створення академії
# my_academy = Academy("MIT", subjects=[math_subject, physics_subject])
#
# # Створення викладачів та студентів
# math_teacher = Teacher("Emely Pennington", 1984, 40, "Mathematics", my_academy)
# physics_teacher = Teacher("Gloria Meyer", 1974, 50, "Physics", my_academy)
# english_teacher = Teacher("Justin Edwards", 1964, 60, "English", my_academy)
#
# student_1 = Student("Lana Branch", 2002, 22, "fg89000", my_academy)
# student_2 = Student("Kira Combs", 2007, 19, "fg89040", my_academy)
#
# # Додавання предметів до академії
# my_academy.add_subject(english_subject)
#
# # Вивід інформації
# student_1.show_info()
# student_2.show_info()
# math_teacher.show_info()
# physics_teacher.show_info()
# english_teacher.show_info()
#
# # Виклик методу для виведення списку предметів
# my_academy.show_subjects()
