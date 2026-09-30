
import numpy as np

dtype=[('roll_no','i4'),
       ('name','U20'),
       ('sem','f8'),
       ('sub_1','i4'),
       ('sub_2','i4'),
       ('sub_3','i4'),
       ('sub_4','i4'),
       ('sub_5','i4')]

data = [(81, "adarsh", 2, 70, 90, 99, 84, 78)]

s = np.array(data, dtype=dtype)[0]

print("\n========== STUDENT MARKSHEET ==========")
print(f"Roll No : {s['roll_no']}")
print(f"Name    : {s['name']}")
print(f"Semester: {s['sem']}")
print("----------------------------------------")
print(" Subject        Marks")
print("----------------------------------------")
print(f" Subject 1     : {s['sub_1']}")
print(f" Subject 2     : {s['sub_2']}")
print(f" Subject 3     : {s['sub_3']}")
print(f" Subject 4     : {s['sub_4']}")
print(f" Subject 5     : {s['sub_5']}")
print("----------------------------------------")

total = s['sub_1'] + s['sub_2'] + s['sub_3'] + s['sub_4'] + s['sub_5']
percentage = total / 5

print(f" Total Marks   : {total}")
print(f" Percentage    : {percentage:.2f}%")
print("========================================\n")

