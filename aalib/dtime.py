import datetime

day = datetime.timedelta(days=1)
week = datetime.timedelta(days=7)


def fmt_dtime(t: datetime.datetime | datetime.date) -> str:
    today = datetime.date.today()

    # check specifically against datetime.date, exclude datetime.datetime
    if type(t) is datetime.date:
        if t == today:
            return "today"
        if t == today + day:
            return "tomorrow"
        if t == today - day:
            return "yesterday"
        if abs(t - today) < week:
            days = abs(t-today).days
            if (t - today).total_seconds() < 0:
                return f"{days} days ago"
            else:
                return f"in {days} days"
        return f"{t:%Y-%m-%d}"

    if t.date() == today:
        return f"today at {t:%H:%M}"
    if t.date() == today + day:
        return f"tomorrow at {t:%H:%M}"
    if t.date() == today - day:
        return f"yesterday at {t:%H:%M}"
    diff = (t.date() - today)
    diff_seconds = diff.total_seconds()
    if abs(diff) < week:
        if diff_seconds < 0:
            # in the past
            return f"{abs(diff.days-1)} days ago at {t:%H:%M}"
        else:
            # in the future
            return f"in {diff.days} days at {t:%H:%M}"
    return f"{t:%Y-%m-%d} at {t:%H:%M}"

if __name__ == '__main__':
    import sys
    d = datetime.datetime.fromisoformat(sys.argv[-1])
    print(fmt_dtime(d))
