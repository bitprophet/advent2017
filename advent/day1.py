def captcha(seq):
    matches = []
    for i, digit in enumerate(seq):
        try:
            next_ = seq[i + 1]
        except IndexError: # wraparound
            next_ = seq[0]
        if digit == next_:
            matches.append(digit)
    return sum(int(x) for x in matches)
