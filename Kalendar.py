import calendar

def print_month_days():
    heute = calendar.datetime.datetime.now()
    jahr, monat = heute.year, heute.month

    kal_monat = calendar.monthcalendar(jahr, monat)
    wochentage = ["MO", "DI", "MI", "DO", "FR", "SA", "SO"]

    kalender_string = ""

    for woche in kal_monat:
        for tag in woche:
            if tag == 0:
                kalender_string += "   " 
            else:
                kalender_string += f"{tag:2d} "

        kalender_string += "\n" 

    return kalender_string

print(print_month_days())
