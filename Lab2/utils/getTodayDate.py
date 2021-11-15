from datetime import date


# get covid date format
def getTodayDate():
    today = date.today()

    # get day
    day = today.strftime("%d")
    dayBefore = int(day) - 1
    day = str(dayBefore)
    # get month
    month = today.strftime("%m")
    # get year
    year = today.strftime("%Y")
    # get last 2 digits of year
    year = str(year)[2:]

    covid_date_format = day + "." + month + "." + year

    return covid_date_format
