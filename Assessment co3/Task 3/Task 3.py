import re

calls = [
    "seeds not received seeds delayed",
    "fertiliser price high",
    "seeds price high subsidy not received"
]

STOP = {"not", "high"}

def frequencies(texts, stop):
    counts = {}

    for text in texts:
        words = re.findall(r"[a-z]+", text.lower())

        for word in words:
            if word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts


def top_words(counts, k):
    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:k]


counts = frequencies(calls, STOP)

print("Frequencies:", counts)
print("Top words:", top_words(counts, 10))


records = [
    {"district": "Madurai", "crop": "rice", "text": "seeds delayed"},
    {"district": "Salem", "crop": "cotton", "text": "fertiliser price"},
    {"district": "Madurai", "crop": "rice", "text": "subsidy pending"}
]


def group_by_district(records):
    grouped = {}

    for record in records:
        grouped.setdefault(record["district"], []).append(record)

    return grouped


print("By district:", group_by_district(records))