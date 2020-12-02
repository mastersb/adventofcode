def main():
    nums = []
    with open('test.txt', 'r') as f:
        for line in f:
            nums.append(int(line))

    # Part 1
    diffs = {}

    for index, item in enumerate(nums):
        diff = 2020 - item

        # if the current item is in diffs,
        # then we previously saw an item that will sum to 2020 with the current item
        # print it and break
        if item in diffs.keys():
            answer = item * diff
            print(f'{item} * {diff} = {answer}')
            break
        else:
            # add the diff to diffs
            diffs[diff] = None

    # Part 2
    nums.sort()

    # iterate over the list
    for index, item in enumerate(nums):
        # set up two pointers
        left = index + 1
        right = len(nums) - 1

        while left < right:
            result = nums[index] + nums[left] + nums[right]

            # move the right pointer inward if we're over 2020
            if result > 2020:
                right -= 1
            # move the left pointer inward if we're under 2020
            elif result < 2020:
                left += 1
            # we found an answer! print it and break
            else:
                answer = nums[index] * nums[left] * nums[right]
                print(f'{nums[index]} * {nums[left]} * {nums[right]} = {answer}')
                break


if __name__ == '__main__':
    main()
