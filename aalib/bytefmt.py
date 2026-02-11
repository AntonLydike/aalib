_suffix = ["", "k", "M", "G", "T", "P", "E", "Z", "Y", "R", "Q"]


def bytefmt(num: int | float, decimal=True):
    base = 1024
    if decimal:
        base = 1000
    i = 0
    while num > base and i < len(_suffix) - 1:
        num /= base
        i += 1
    # whole numbers:
    if num % 1 < 0.01:
        nums = str(int(num))
    elif num < 10:
        nums = format(num, ".2f")
    elif num < 100:
        nums = format(num, ".1f")
    else:
        nums = str(int(num))

    if i == 0:
        return f"{nums}B"
    if not decimal:
        return f"{nums}{_suffix[i].upper()}iB"
    return f"{nums}{_suffix[i]}B"
