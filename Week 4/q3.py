students = {
    "Ahmad": 82,
    "Adnan": 67,
    "Atif": 91,
    "Hasan": 74,
    "Tameem": 88
}
print("Students scoring above 75:")

for name, marks in students.items():
    if marks > 75:
        print(f"{name}: {marks}")
