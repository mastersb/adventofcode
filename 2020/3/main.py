def main():

    grid = []
    # Create grid
    with open('input.txt', 'r') as f:
        for line in f:
            grid.append(list(line.strip()))

    # Part 1
    trees_hit_part_1 = toboggan_time(grid, 3, 1)
    print(f'Part 1: {trees_hit_part_1}')

    # Part 2
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = []

    for s in slopes:
        trees.append(toboggan_time(grid, s[0], s[1]))

    trees_hit_part_2 = 1
    for t in trees:
        trees_hit_part_2 *= t

    print(f'Part 2: {trees_hit_part_2}')


def toboggan_time(grid, right, down):
    trees_hit = 0
    row = 0
    col = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    while row < (num_rows - 1):
        col = col + right
        # wrap around in the same row if need-be
        if col > (num_cols - 1):
            col = col - num_cols

        if grid[row+down][col] == '#':
            trees_hit += 1

        row += down

    return trees_hit


if __name__ == '__main__':
    main()
