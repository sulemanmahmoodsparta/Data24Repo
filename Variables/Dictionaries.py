# ----- Key ---> Value
# --- E.g. In an actually dictionary: The Key would be the word and the Value would a greeting.
# Look up the key to find the value.
# Keys can't be repeated/ no duplicates.

student_1 = {"name": "Susan",
             "stream": "tech",
             "completed_lessons": 4,
             "completed_lesson_names": ["variables", "data_types", "dictionaries"]
             }

print(student_1["stream"])
print(student_1["completed_lesson_names"][1])
print(student_1["completed_lesson_names"][1][1])

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

# ---Removal

student_1["completed_lesson_names"].remove("data_types")

print(student_1["completed_lesson_names"])

print(student_1.keys())
print(student_1.values())