#task1:- "create dict"
student_grades = {
       "mariya": 85,
       "soumya": 78,
       "ramar":  62,
}
print("student grades:-", student_grades)

#task:- 2
alice_grade = student_grades["mariya"]
print("mariya's grade:-", alice_grade)

#task:- 3
student_grades["rashmi"] = 88
print("updated  student grades:-", student_grades)

#task:- 4
student_grades.pop("soumya")
print("after poping soumya:-",student_grades)

#task:- 5
is_ramar_in_dict = "meera" in student_grades
print("is meera in student grades:-", is_ramar_in_dict)

#task:- 6
for student, grade in student_grades.items():
    print(f"[{student} -:- {grade}")

#task 7:-
david_grade = student_grades.get("ramar",)
print("ramar's grade:-", david_grade)

#task:- 8
additional_grade = {"kavya":- 76, "mahi":- 89}
student_grades.update(additional_grade)
print("student grades after updated:-", student_grades)

#task:- 9
sqared_nums = {x: x **2 for x in range(2,11,2)}
print("dict. of nums and their squares-",sqared_nums)

#task:- 10
nested_dict = {
     "USA": {"new york": 8000000, "los angeles": 4000000},
     "india": {"mumbai": 2000000, "delhi":15000000},
}
print("nested dict of countries and cities:-", nested_dict)


ny_population = nested_dict["USA"]["new york"]
print("population of new york:-", ny_population)

#task:- 11
st_grades_copy = student_grades.copy()
print("copy of st grades:-", st_grades_copy)

st_grades_copy.clear()
print(st_grades_copy)