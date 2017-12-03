from itertools import combinations


def string_to_lists(sheet):
    """
    Turn a string-formatted 'spreadsheet' into a 2D array of integers.

    The personal input is tab-separated but the example is not, so we just do
    regular ol generic whitespace splitting.
    """
    return [[int(y) for y in x.split()] for x in sheet.strip().splitlines()]


def checksum(sheet):
    data = string_to_lists(sheet)
    return sum(max(row) - min(row) for row in data)


def evenly_divisible_checksum(sheet):
    data = string_to_lists(sheet)
    matches = []
    for row in data:
        # Reverse-sort so the math becomes larger / smaller
        for combo in combinations(sorted(row, reverse=True), 2):
            quotient, remainder = divmod(*combo)
            if remainder is 0:
                # Problem states only one such pair per row
                matches.append(quotient)
                break
    return sum(matches)
