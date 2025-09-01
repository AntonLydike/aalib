from math import floor, log

_dur_to_prefix_small = {
    0: "s",
    -1: "ms",
    -2: "μs",
    -3: "ns",
    -4: "ps",
    -5: "fs",
    -6: "as",
    -7: "zs",
}
_time_divisions = (
    (60, "m"),
    (60, "h"),
    (24, "d"),
    (365.25 / 12, "mo"),
    (12, "y"),
    (100, "century"),
)


def duration(dur_in_seconds: float, map_nan:str = "NaN") -> str:
    """
    Convert a duration in seconds to a string

    :param dur_in_seconds:
    :return:
    """
    # check NaN
    if dur_in_seconds != dur_in_seconds:
        return map_nan
    if dur_in_seconds <= 0:
        return "0s"
    if dur_in_seconds < 60:
        exp = floor(log(dur_in_seconds, 1000))
        if exp not in _dur_to_prefix_small:
            return f"{dur_in_seconds}s"
        ttl = dur_in_seconds / pow(1000, exp)
        sfx = _dur_to_prefix_small[exp]
        return f"{ttl:.3g}{sfx}".lstrip()

    last_num, last_suf = 0, "ms"
    num, suf = dur_in_seconds, "s"
    for div, new_suf in _time_divisions:
        if num < div:
            if last_num < 1:
                if round(num) == num:
                    return f"{round(num)}{suf}"
                return f"{num:.3g}{suf}"
            return f"{floor(num)}{suf}{round(last_num)}{last_suf}"
        last_suf = suf
        last_num = num % div
        num /= div
        suf = new_suf

    if last_num < 1:
        if round(num) == num:
            num = round(num)
        return f"{num:.3g}{suf}"
    return f"{round(num)}{suf}{round(last_num)}{last_suf}"
