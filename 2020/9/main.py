def main():
    preamble_size = 25  # 5 for test.txt, 25 for input.txt
    numbers = []
    diffs = {}
    bad_sum = -1

    with open('input.txt', 'r') as f:
        for line in f:
            numbers.append(int(line.strip()))

    # print(numbers)
    # Part 1
    lower_bound = 0
    for i in range(preamble_size, len(numbers)):
        result = sum_exists(numbers[lower_bound : i], numbers[i])

        if not result:
            bad_sum = numbers[i]
            break

        lower_bound += 1

    print(f'Part 1: {numbers[i]}')

    # Part 2
    lptr = 0
    rptr = 1
    total = 0
    while total != bad_sum:
        total = numbers[lptr]
        for i in range((lptr + 1), len(numbers)):
            total += numbers[i]
            rptr = i
            if total == bad_sum:
                break

            if total > bad_sum:
                lptr += 1
                break

    weakness = numbers[lptr : rptr]
    small = min(weakness)
    large = max(weakness)

    print(f'Part 2: {small + large}')



# 2Sum technique
def sum_exists(numbers, num):
    diffs = {}
    for index, number in enumerate(numbers):
        diff = num - number
        if diff in diffs:
            return True

        diffs[number] = index

    return False


if __name__ == '__main__':
    main()
