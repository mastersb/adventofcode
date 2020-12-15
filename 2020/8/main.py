def main():
    program = []

    with open('input.txt', 'r') as f:
        for line in f:
            program.append(line.strip())

    # print(program)
    # print(counter)

    # Part 1
    code, acc = computer(program)
    print(f'Part 1: Code: {code} Accumulator: {acc}')

    # Part 2
    for index, instruction in enumerate(program):
        parsed = parse_instruction(instruction)
        if parsed[0] == 'nop':
            parsed[0] = 'jmp'
        elif parsed[0] == 'jmp':
            parsed[0] = 'nop'

        new_ins = create_instruction(parsed)
        program[index] = new_ins
        print(f'{instruction} -> {new_ins}')

        # execute the new code
        code, acc = computer(program)
        if code == -1:
            program[index] = instruction  # restore the original instruction
        elif code == 0:
            print(f'Part 2: Code: {code} Accumulator: {acc}')
            break


def computer(program):
    pc = 0
    accumulator = 0
    counter = []
    for i in range(len(program)):
        counter.append(0)

    while pc < len(program) and counter[pc] < 1:
        counter[pc] += 1
        ins = parse_instruction(program[pc])
        if ins[0] == 'acc':
            if ins[1] == '+':
                accumulator += ins[2]
            else:
                accumulator -= ins[2]
            pc += 1

        if ins[0] == 'jmp':
            if ins[1] == '+':
                pc += ins[2]
            else:
                pc -= ins[2]

        if ins[0] == 'nop':
            pc += 1

    if pc < len(program):
        return [-1, accumulator]
    else:
        return [0, accumulator]


def parse_instruction(ins):
    parts = ins.partition(' ')
    plus_minus = parts[2][:1]
    number = parts[2][1:]
    return [parts[0], plus_minus, int(number)]


def create_instruction(parts):
    return parts[0] + ' ' + parts[1] + str(parts[2])


if __name__ == '__main__':
    main()
