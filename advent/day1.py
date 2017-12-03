def captcha(seq, selector):
    """
    Generic captcha algo that uses a selector function.
    """
    matches = []
    for i, digit in enumerate(seq):
        if digit == selector(i, seq):
            matches.append(digit)
    return sum(int(x) for x in matches)


def captcha_next(seq):
    """
    First captcha which checks digits against the next digit in sequence.
    """
    def selector(i, seq):
        try:
            next_ = seq[i + 1]
        except IndexError: # wraparound
            next_ = seq[0]
        return next_
    return captcha(seq, selector)


def captcha_opposite(seq):
    def selector(i, seq):
        # Halfway is how far away? (May assume even size.)
        halfway = int(len(seq) / 2)
        # Make a double-wide seq that can be indexed in such a way.
        doublewide = seq + seq
        # And look there.
        return doublewide[i + halfway]
    return captcha(seq, selector)
