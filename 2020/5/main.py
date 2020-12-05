def main():
    seat_ids = []

    with open('input.txt', 'r') as f:
        for line in f:
            row = find_row(line[:7])
            col = find_col(line[7:])
            seat_id = (row * 8) + col
            seat_ids.append(seat_id)
            # print(f'{line.strip()}: row {row}, column {seat}, seat ID {seat_id}')

        seat_ids.sort()
        my_seat_id = find_seat(seat_ids)

        print(f'Part 1: Max Seat ID: {seat_ids[-1]}')
        print(f'Part 2: My Seat ID: {my_seat_id}')


def find_row(row_data):
    low = 0
    high = 127
    for c in row_data:
        if c == 'F':
            high = ((high - low) // 2) + low
        elif c == 'B':
            low = ((high - low) // 2) + low + 1

    return low


def find_col(col_data):
    low = 0
    high = 7
    for c in col_data:
        if c == 'L':
            high = ((high - low) // 2) + low
        elif c == 'R':
            low = ((high - low) // 2) + low + 1

    return low


def find_seat(seat_ids):
    i = seat_ids[0]     # Starting Seat ID
    for s in seat_ids:
        if s != i:
            break
        i += 1

    return i


if __name__ == '__main__':
    main()
