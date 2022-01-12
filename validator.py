"""
This is a python validator program.
Intent is to validate a string to see if the given string is a valid nric/fin number.
"""


def get_data(file):
    with open(file) as f:
        data = f.readlines()
    return data


def compute_nric_checksum(val):
    switch = {
        0: 'J',
        1: 'Z',
        2: 'I',
        3: 'H',
        4: 'G',
        5: 'F',
        6: 'E',
        7: 'D',
        8: 'C',
        9: 'B',
        10: 'A'
    }
    return switch.get(val)


def compute_fin_checksum(val):
    switch = {
        0: 'X',
        1: 'W',
        2: 'U',
        3: 'T',
        4: 'R',
        5: 'Q',
        6: 'P',
        7: 'N',
        8: 'M',
        9: 'L',
        10: 'K'
    }
    return switch.get(val)


def compute_checksum(input_str):
    val01 = int(input_str[1]) * 2
    val02 = int(input_str[2]) * 7
    val03 = int(input_str[3]) * 6
    val04 = int(input_str[4]) * 5
    val05 = int(input_str[5]) * 4
    val06 = int(input_str[6]) * 3
    val07 = int(input_str[7]) * 2

    checksum = val01 + val02 + val03 + val04 + val05 + val06 + val07
    print("Computed checksum : ", checksum)
    return checksum


def validate_identity_id(input_str):
    status = ""
    if len(input_str) != 9:
        status = "Fail String Length!"

    checksum = compute_checksum(input_str)

    if input_str[0] == 'T' or input_str[0] == 'G':
        checksum = checksum + 4
    elif input_str[0] == 'M':
        checksum = checksum + 3

    y = checksum % 11

    if input_str[0] == 'S' or input_str[0] == 'T':
        check_digit = compute_nric_checksum(y)

        if input_str[8] == check_digit:
            status = "Success - Valid NRIC."
        else:
            status = "Fail - Invalid NRIC."
    elif input_str[0] == 'F' or input_str[0] == 'G' or input_str[0] == 'M':
        check_digit = compute_fin_checksum(y)

        if input_str[8] == check_digit:
            status = "Success- Valid FIN."
        else:
            status = "Fail - Invalid FIN."

    print("checksum + offset (if any):", checksum)
    print("position:", y)
    print("Check Digit:", check_digit)
    return status


def main():
    list_of_ids = get_data("data.txt")

    for i in list_of_ids:
        identifier = i.strip()
        outcome = validate_identity_id(identifier)
        print("id=[", identifier, "], outcome=[", outcome, "].")

# Execute main
main()
