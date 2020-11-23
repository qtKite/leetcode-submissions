def isNumber(s):
    # can only contain 1 e
    # only one decimal
    # no other chars allowed
    # only one sign bit which is the left most
    # can contain spaces on left and right and not in between

    s = s.strip()
    decimal_count = 0
    e_count = 0
    e_pos = 0
    sign_count = 0
    sign_pos = 0
    index = 0
    num_arr = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    has_error = False
    num_of_nums = 0

    for i in s:
        if i == '-':
            sign_count += 1
            sign_pos = index

        if i == '+':
            sign_count += 1
            sign_pos = index

        if i not in num_arr:
            if i != 'e':
                if i != '.':
                    has_error = True
            else:
                e_count += 1
                e_pos = index
        else:
            num_of_nums += 1

        if i == '.':
            decimal_count += 1

        index += 1

    if e_count > 1:
        print("1")
        has_error = True

    if e_count == 1 and num_of_nums == 0:
        print("2")
        has_error = True

    if e_count >= 1 and e_pos == 0:
        print("3")
        has_error = True

    if sign_count > 1:
        print("4")
        has_error = True

    if sign_count == 1 and sign_pos != 0:
        print("5")
        has_error = True

    if decimal_count > 1:
        print("6")
        has_error = True

    if num_of_nums == 0:
        print("7")
        has_error = True

    return not has_error

print(isNumber('-1.'))
