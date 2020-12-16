import calendar


def pythagorean_triple(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def pythagorean_dates(start_year, end_year):
    dates = []
    c = calendar.Calendar()
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            for day in (d for d in c.itermonthdays(year, month) if d != 0):
                if pythagorean_triple(day, month, year % 100):
                    dates.append((day, month, year))
    return dates


if __name__ == "__main__":
    print(pythagorean_dates(2000, 2099))