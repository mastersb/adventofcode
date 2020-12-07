def main():
    groups_part_1 = []
    groups_part_2 = []
    with open('input.txt', 'r') as f:
        group_size = 0
        answers = ''
        for line in f:
            if line == '\n':
                groups_part_1.append(combine_answers(answers))
                groups_part_2.append(combine_answers_part_2(answers, group_size))
                group_size = 0
                answers = ''
            else:
                answers += line.strip()
                group_size += 1

        groups_part_1.append(combine_answers(answers))
        groups_part_2.append(combine_answers_part_2(answers, group_size))

        print(f'Part 1: {sum(groups_part_1)}')
        print(f'Part 2: {sum(groups_part_2)}')


def combine_answers(answers):
    a = set()
    for c in answers:
        a.add(c)

    return len(a)


def combine_answers_part_2(answers, size):
    a = {}

    for c in answers:
        if c in a.keys():
            a[c] += 1
        else:
            a[c] = 1

    out = 0
    for c in answers:
        if a[c] == size:
            out += 1
            a[c] = -1

    return out


if __name__ == '__main__':
    main()
