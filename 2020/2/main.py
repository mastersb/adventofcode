def main():
    valid_passwords_1 = 0
    valid_passwords_2 = 0

    with open('input.txt', 'r') as f:
        for line in f:
            partition1 = line.partition('-')           # ('1', '-', '3 a: abcde')
            partition2 = partition1[2].partition(' ')  # ('3', ' ', 'a: abcde')
            partition3 = partition2[2].partition(':')  # ('a', ':', ' abcde')

            low = int(partition1[0])
            high = int(partition2[0])
            key = partition3[0]
            password = partition3[2].strip()

            valid_1 = is_valid(low, high, key, password)
            valid_2 = is_valid_part_two(low, high, key, password)

            if valid_1:
                valid_passwords_1 += 1

            if valid_2:
                valid_passwords_2 += 1

            # print(low, high, key, password, valid_1, valid_2)

    print(f'valid passwords for part 1: {valid_passwords_1}')
    print(f'valid passwords for part 2: {valid_passwords_2}')


def is_valid(low, high, key, password):
    count = 0
    for c in password:
        if c == key:
            count += 1

    if low <= count <= high:
        return True

    return False


def is_valid_part_two(position1, position2, key, password):
    count = 0
    if password[position1 - 1] == key:
        count += 1

    if password[position2 - 1] == key:
        count += 1

    if count == 1:
        return True

    return False


if __name__ == '__main__':
    main()
