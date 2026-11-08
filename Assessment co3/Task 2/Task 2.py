import sys
import timeit
import copy

rows, cols = 3, 4

bad = [[0] * cols] * rows

bad[0][1] = 7

print("Bad grid:", bad)
print("Same row object:", bad[0] is bad[1])

good = [[0 for c in range(cols)] for r in range(rows)]

good[0][1] = 7

print("Good grid:", good)
print("Same row object:", good[0] is good[1])

stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print("Location:", stops[(13.0418, 80.2341)])

try:
    stops[[13.0418, 80.2341]] = "T. Nagar"
except TypeError as e:
    print("Error:", e)

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 99
deep[1][0] = 88

print("Original:", original)
print("Shallow copy:", shallow)
print("Deep copy:", deep)

values = list(range(1000000))
tuple_values = tuple(values)

print("List memory:", sys.getsizeof(values))
print("Tuple memory:", sys.getsizeof(tuple_values))

list_time = timeit.timeit(
    'values[500000]', globals=globals(), number=1000000
)

tuple_time = timeit.timeit(
    'tuple_values[500000]', globals=globals(), number=1000000
)

print("List indexing time:", list_time)
print("Tuple indexing time:", tuple_time)

data = ([1, 2], [3, 4])

data[0].append(5)

print("Modified tuple:", data)