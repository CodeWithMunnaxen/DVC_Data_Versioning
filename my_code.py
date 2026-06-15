import pandas as pd

df = pd.read_csv("data\students.csv")

name = input("Enter student name: ")
marks = int(input("Enter marks: "))

new_student = {
    "name": name,
    "marks": marks
}

df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)

df.to_csv("data/students.csv", index=False)

print("Student added successfully!")
print(df)