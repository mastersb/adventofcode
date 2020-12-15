def main():
    adapters = []
    joltages = [0, 0, 0, 1]

    with open('test2.txt', 'r') as f:
        for line in f:
            adapters.append(int(line))

    adapters.sort()
    print(adapters)

    # Part 1
    for index, joltage in enumerate(adapters):
        if index == 0:
            diff = joltage - 0
            joltages[diff] += 1
        else:
            diff = joltage - adapters[index - 1]
            joltages[diff] += 1

    print(joltages)
    print(f'Part 1: {joltages[1] * joltages[3]}')

    # Part 2


if __name__ == '__main__':
    main()
