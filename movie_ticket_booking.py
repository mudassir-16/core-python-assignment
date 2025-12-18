def book_seat(booked_seats, seat_number, total_seats):
    if 1 <= seat_number <= total_seats and seat_number not in booked_seats:
        booked_seats.append(seat_number)


def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)


def available_seats(total_seats, booked_seats):
    return [i for i in range(1, total_seats + 1) if i not in booked_seats]


total_seats = 10
booked_seats = [2, 5, 7]

book_seat(booked_seats, 3, total_seats)
cancel_seat(booked_seats, 5)

print("Available seats:", available_seats(total_seats, booked_seats))
