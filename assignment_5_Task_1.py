marks_dict = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88,
    "Emma": 90
}


name = input("Enter the student's name: ")
present = False

for nam in marks_dict:
    if name in nam:
        present = True
        break
    else:
        present = False

if( present==True):
    print(f"{name}'s marks: {marks_dict[name]}")
else:
    print("Student not found.")