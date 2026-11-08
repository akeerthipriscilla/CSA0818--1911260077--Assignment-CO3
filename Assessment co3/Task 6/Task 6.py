timetable = {
    "12601": [
        {"station": "Chennai Central", "arrival": None, "departure": "06:00"},
        {"station": "Katpadi", "arrival": "07:35", "departure": "07:40"},
        {"station": "Jolarpettai", "arrival": "09:05", "departure": "09:10"},
        {"station": "Bengaluru", "arrival": "11:00", "departure": None}
    ],
    "12602": [
        {"station": "Chennai Central", "arrival": None, "departure": "08:00"},
        {"station": "Katpadi", "arrival": "09:30", "departure": "09:35"},
        {"station": "Salem", "arrival": "12:00", "departure": "12:05"}
    ]
}

for train_no, stops in timetable.items():
    print("\nTrain:", train_no)
    for stop in stops:
        print(stop["station"], stop["arrival"], stop["departure"])

# Departure from the third station (index 2)
train_no = "12601"
third = timetable[train_no][2]
print("Third station:", third["station"])
print("Departure:", third["departure"])

# Build a station index
station_index = {}
for train_no, stops in timetable.items():
    for position, stop in enumerate(stops):
        station_index.setdefault(stop["station"], []).append(
            (train_no, position)
        )

print("Trains serving Katpadi:", station_index.get("Katpadi", []))

# Sort one train's stops by departure time; None values are placed last.
ordered = sorted(
    timetable["12601"],
    key=lambda s: s["departure"] or "99:99"
)
print("Sorted stations:", [s["station"] for s in ordered])

