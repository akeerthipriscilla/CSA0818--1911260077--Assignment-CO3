a1 = {"20231001", "20231002", "20231003", "20231003"}
a2 = {"20231002", "20231004"}
all_students = {"20231001", "20231002", "20231003",
                "20231004", "20231005"}

both = a1 & a2
either = a1 | a2
only_a1 = a1 - a2
exactly_one = a1 ^ a2
not_registered = all_students - either

print("Both:", sorted(both))
print("Union:", sorted(either))
print("Only elective 1:", sorted(only_a1))
print("Exactly one:", sorted(exactly_one))
print("Not registered:", sorted(not_registered))

students_list = list(all_students)
students_set = set(all_students)
print("List membership:", "20231003" in students_list)
print("Set membership:", "20231003" in students_set)
