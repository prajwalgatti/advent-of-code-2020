# day 4

# Part 1

with open("input.txt", 'r') as f:
    # format data into list of dictionaries
    # where each dictionary is a passport
    data = [dict(entry.split(":") for entry in data.split())
            for data in f.read().split("\n\n")]

num_valid_passports = 0

REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
OPT_FIELDS = {'cid'}

for passport in data:
    if REQUIRED_FIELDS.difference(passport.keys()).issubset(OPT_FIELDS):
        num_valid_passports += 1

print("Part 1")
print("Number of valid passports: {}".format(num_valid_passports))

# Part 2

num_valid_passports_2 = 0

for passport in data:
    try:
        # check for byr
        byr = len(passport['byr']) == 4 and 1920 <= int(
            passport['byr']) <= 2002

        # check for iyr
        iyr = len(passport['iyr']) == 4 and 2010 <= int(
            passport['iyr']) <= 2020

        # check for eyr
        eyr = len(passport['eyr']) == 4 and 2020 <= int(
            passport['eyr']) <= 2030

        # check for hcl
        hcl = len(passport['hcl']) == 7 and passport['hcl'].startswith('#')
        int(passport['hcl'][1:], 16)

        # check for ecl
        ecl = passport['ecl'] in {"amb", "blu",
                                  "brn", "gry", "grn", "hzl", "oth"}
        # check for pid
        pid = len(passport['pid']) == 9 and passport['pid'].isnumeric()

        # check for hgt
        if passport['hgt'].endswith('cm'):
            hgt = 150 <= int(passport['hgt'][:-2]) <= 193
        elif passport['hgt'].endswith('in'):
            hgt = 59 <= int(passport['hgt'][:-2]) <= 76
        else:
            hgt = False

        if all({byr, iyr, eyr, hcl, ecl, pid, hgt}):
            num_valid_passports_2 += 1

    except (ValueError, KeyError):
        pass

print("Part 2")
print("Number of valid passports: {}".format(num_valid_passports_2))
