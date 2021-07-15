def dateCheck(date):
    numDate = date.split(".")
    if (int(numDate[0]) >= 12 or int(numDate[1]) >= 12 ):
        return ("Non-Ambiguous")
    elif (int(numDate[0]) == int(numDate[1])):
        return ("Non-Ambiguous")
    else:
        return ("Ambiguous")
def validDate(day, month):
    thirtyDayMonths = [4, 6, 9, 11]
    if day > 31 or month > 12 or day < 0 or month < 0:
        return False
    if (month == 2 and day > 28):
        return False
    if (month!=2 and month in thirtyDayMonths and day > 30):
        return False
    return True
date = "15.08.2021"
dateCheck(date)
ambiguous = []
nonAmbiguous = []
def yearDates():
    mm = [i for i in range(1,13)]
    dd = [i for i in range(1,32)]
    year = 2021
    for month in mm:
        for day in dd:
            formatedDate = f'{day}.{month}.{year}'
            if validDate(day, month):
                if(dateCheck(formatedDate) == "Ambiguous"):
                    ambiguous.append(formatedDate)
                else:
                    nonAmbiguous.append(formatedDate)
yearDates()
print(ambiguous)
print(nonAmbiguous)