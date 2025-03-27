# Female Students
female_students = [
    {"name": "Evelyn", "height": 5.5, "age": 17, "score": 80},
    {"name": "Jessica", "height": 6.0, "age": 16, "score": 85},
    {"name": "Somto", "height": 5.4, "age": 17, "score": 70},
    {"name": "Edith", "height": 5.9, "age": 18, "score": 60},
    {"name": "Liza", "height": 5.6, "age": 16, "score": 76},
    {"name": "Madonna", "height": 5.5, "age": 18, "score": 66},
    {"name": "Waje", "height": 6.1, "age": 17, "score": 87},
    {"name": "Tola", "height": 6.0, "age": 20, "score": 95},
    {"name": "Aisha", "height": 5.7, "age": 19, "score": 50},
    {"name": "Latifa", "height": 5.5, "age": 17, "score": 49}
]

# Male Students
male_students = [
    {"name": "Chinedu", "height": 5.7, "age": 19, "score": 74},
    {"name": "Liam", "height": 5.9, "age": 16, "score": 87},
    {"name": "Wale", "height": 5.8, "age": 18, "score": 75},
    {"name": "Gbenga", "height": 6.1, "age": 17, "score": 68},
    {"name": "Abiola", "height": 5.9, "age": 20, "score": 66},
    {"name": "Kola", "height": 5.5, "age": 19, "score": 78},
    {"name": "Kunle", "height": 6.1, "age": 16, "score": 87},
    {"name": "George", "height": 5.4, "age": 18, "score": 98},
    {"name": "Thomas", "height": 5.8, "age": 17, "score": 54},
    {"name": "Wesley", "height": 5.7, "age": 19, "score": 60}
]
students = female_students + male_students
print("STUDENT RECORDS\n")
print(f"{'NAME':<10} | {'HEIGHT':<10} | {'AGE':<10} | {'SCORE':<10}")
print("-" * 40)

for student in students:
    print(f"{student['name']:<10}|{student['height']:<10}|{student['age']:<10}|{student['score']:<10}|")

