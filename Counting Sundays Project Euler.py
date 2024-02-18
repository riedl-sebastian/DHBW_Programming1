import datetime

def cs(start, end):
    sundays = 0
    for year in range(start, end + 1):
        for month in range(1, 13):
            if datetime.datetime(year, month, 1).weekday() == 6:
                sundays += 1
    return sundays

# Testen der Funktion
start_year = 1901
end_year = 2000
print(cs(start_year, end_year))
