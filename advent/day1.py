def captcha_next(seq):
    """
    First captcha which checks digits against the next digit in sequence.
    """
    matches = []
    for i, digit in enumerate(seq):
        try:
            next_ = seq[i + 1]
        except IndexError: # wraparound
            next_ = seq[0]
        if digit == next_:
            matches.append(digit)
    return sum(int(x) for x in matches)
