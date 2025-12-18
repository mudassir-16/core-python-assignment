def book_seat(booked, seat, total):
    if 1 <= seat <= total and seat not in booked:
        booked.append(seat)


def cancel_seat(booked, seat):
    if seat in booked:
        booked.remove(seat)


def available_seats(total, booked):
    return [i for i in range(1, total + 1) if i not in booked]


total_seats = int(input("Enter total seats: "))
booked_seats = list(map(int, input("Enter booked seats separated by space: ").split()))

book = int(input("Enter seat to book: "))
cancel = int(input("Enter seat to cancel: "))

book_seat(booked_seats, book, total_seats)
cancel_seat(booked_seats, cancel)

print("Available seats:", available_seats(total_seats, booked_seats))
