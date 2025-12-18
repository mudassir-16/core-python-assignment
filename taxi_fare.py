def calculate_fare(distance):
    return 50 + distance * 10


trips = list(map(int, input("Enter trip distances separated by space: ").split()))
total = 0

for i, d in enumerate(trips, 1):
    fare = calculate_fare(d)
    total += fare
    print(f"Trip {i}: ${fare}")

print(f"Total Fare: ${total}")
