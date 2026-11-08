import sys

readings = [22, -60, 35, 51, -50, 0, 50, 22, 99, -12]

# Version 1: plain loop
valid_loop = []
for c in readings:
    if -50 <= c <= 50:
        valid_loop.append(c)

# Version 2: list comprehension
# general form: [expression for item in iterable if condition]
valid_list = [c for c in readings if -50 <= c <= 50]

# Version 3: generator expression (round brackets, lazy)
valid_gen = (c for c in readings if -50 <= c <= 50)

# Dictionary comprehension: index -> valid reading
valid_dict = {i: c for i, c in enumerate(readings) if -50 <= c <= 50}

# Set comprehension: distinct valid readings
valid_set = {c for c in readings if -50 <= c <= 50}

print("Loop     :", valid_loop)
print("List comp:", valid_list)
print("Generator:", list(valid_gen))
print("Dict comp:", valid_dict)
print("Set comp :", sorted(valid_set))

print("Identical results:", valid_loop == valid_list == [c for c in readings if -50 <= c <= 50])

print("List memory     :", sys.getsizeof(valid_list), "bytes")
print("Generator memory:", sys.getsizeof((c for c in readings if -50 <= c <= 50)), "bytes")

# sum() with a generator (no list is built)
print("Sum of valid readings:", sum(c for c in readings if -50 <= c <= 50))

