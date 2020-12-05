def main():
    valid_passports_part_1 = 0
    valid_passports_part_2 = 0

    with open('input.txt', 'r') as f:
        passport_string = ''
        for line in f:
            if line == '\n':
                passport = create_passport_dict(passport_string)
                valid_passports_part_1 += 1 if validate_passport_part_1(passport) else 0
                valid_passports_part_2 += 1 if validate_passport_part_2(passport) else 0
                passport_string = ''
            else:
                passport_string += line.strip() + ' '

        # Process the last line in the file
        passport = create_passport_dict(passport_string)
        valid_passports_part_1 += 1 if validate_passport_part_1(passport) else 0
        valid_passports_part_2 += 1 if validate_passport_part_2(passport) else 0

    print(f'Part 1: {valid_passports_part_1}')
    print(f'Part 2: {valid_passports_part_2}')


def create_passport_dict(passport_string):
    passport_string = passport_string.strip()
    passport = {}
    for p in passport_string.split(' '):
        colon = p.find(':')
        key = p[0: colon]
        value = p[colon + 1:]
        passport[key] = value

    return passport


def validate_passport_part_1(passport):
    if 'byr' in passport.keys() and \
            'iyr' in passport.keys() and \
            'eyr' in passport.keys() and \
            'hgt' in passport.keys() and \
            'hcl' in passport.keys() and \
            'ecl' in passport.keys() and \
            'pid' in passport.keys():
        # print(f'valid 1: {passport}')
        return True

    # print(f'invalid 1: {passport}')
    return False


def validate_passport_part_2(passport):
    if 'byr' in passport.keys() and validate_byr(passport['byr']) and \
            'iyr' in passport.keys() and validate_iyr(passport['iyr']) and \
            'eyr' in passport.keys() and validate_eyr(passport['eyr']) and \
            'hgt' in passport.keys() and validate_hgt(passport['hgt']) and \
            'hcl' in passport.keys() and validate_hcl(passport['hcl']) and \
            'ecl' in passport.keys() and validate_ecl(passport['ecl']) and \
            'pid' in passport.keys() and validate_pid(passport['pid']):
        # print(f'valid 2: {passport}')
        return True

    # print(f'invalid 2: {passport}')
    return False


def validate_byr(year):
    return 1920 <= int(year) <= 2002


def validate_iyr(year):
    return 2010 <= int(year) <= 2020


def validate_eyr(year):
    return 2020 <= int(year) <= 2030


def validate_hgt(height):
    if len(height) < 4:
        return False

    unit = height[-2:]
    value = int(height[:-2])
    if unit == 'cm':
        return 150 <= value <= 193
    elif unit == 'in':
        return 59 <= value <= 76
    else:
        return False


def validate_hcl(color):
    if len(color) == 7 and color[0] == '#':
        return True

    return False


def validate_ecl(color):
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return color in valid_colors


def validate_pid(id):
    return len(id) == 9


if __name__ == '__main__':
    main()
