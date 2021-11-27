def find_key(roll, table):
    for key in table:
        if key <= roll:
            candidate = key
    return candidate
