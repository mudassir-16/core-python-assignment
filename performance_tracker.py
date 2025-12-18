def calculate_average(marks):
    return sum(marks) / len(marks)


students = {}
n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks separated by space: ").split()))
    students[name] = marks

averages = {}
topper = ""
highest = 0

for name, marks in students.items():
    avg = calculate_average(marks)
    averages[name] = round(avg, 2)
    if avg > highest:
        highest = avg
        topper = name

print("Average Marks:", averages)
print("Top Performer:", topper)
