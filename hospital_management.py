patients = []
n = int(input("Enter number of patients: "))

for _ in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    disease = input("Enter disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})

search = input("Enter disease to search: ")

result = [p["Name"] for p in patients if p["Disease"] == search]
print(f"Patients with {search}:", result)
