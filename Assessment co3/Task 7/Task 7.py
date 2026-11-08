import re
import time

contacts = [
    {"name": "Dr. Ravi", "phone": "+91 90000 12345", "email": "ravi@mail.com"},
    {"name": "Ravi", "phone": "9000012345", "email": ""},
    {"name": "Meena", "phone": "98765 43210", "email": "meena@mail.com"},
    {"name": "MEENA", "phone": "+91-9876543210", "email": "meena@work.com"}
]

def clean_name(name):
    return re.sub(r"[^a-z]", "", name.lower())

def clean_phone(phone):
    return re.sub(r"\D", "", phone)

def merge_contacts(records):
    merged = {}
    for record in records:
        key = clean_name(record["name"])
        if key not in merged:
            merged[key] = {
                "name": record["name"],
                "phones": [],
                "emails": []
            }

        phone = clean_phone(record.get("phone", ""))
        email = record.get("email", "").strip().lower()

        if phone and phone not in merged[key]["phones"]:
            merged[key]["phones"].append(phone)
        if email and email not in merged[key]["emails"]:
            merged[key]["emails"].append(email)

    return list(merged.values())

start = time.perf_counter()
result = merge_contacts(contacts)
elapsed = time.perf_counter() - start

for contact in result:
    print(contact)
print("Merge time:", elapsed)

def pair_count(n):
    return n * (n - 1) // 2

print("Pair comparisons for 1000:", pair_count(1000))
print("Pair comparisons for 100000:", pair_count(100000))
