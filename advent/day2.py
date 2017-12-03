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
