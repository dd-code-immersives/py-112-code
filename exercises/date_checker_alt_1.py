
def ambiguous_date(date):
    
    Sdate = date.split('.')
    Ndate = [int(d) for d in Sdate]
    
    first = Ndate[0]
    second = Ndate[1]
    third = Ndate[2]

    if third != 2021:
        return f"Invalid entry only checking year 2021"
    elif first == second:
        return f"{date} Is non-ambigous"
    elif first == 2 and second > 28:
        return f"Try again {date} is an invalid date"
    elif first > 28 and second == 2:
        return f"Try again {date} is an invalid date"
    elif first == 4 and second > 30:
        return f"Try again {date} is an invalid date"
    elif first == 6 and second > 30:
        return f"Try again {date} is an invalid date"
    elif first == 9 and second > 30:
        return f"Try again {date} is an invalid date"
    elif first == 11 and second > 30:
        return f"Try again {date} is an invalid date"
    elif first > 30 and second == 4:
        return f"Try again {date} is an invalid date"
    elif first > 30 and second == 6:
        return f"Try again {date} is an invalid date"
    elif first > 30 and second == 9:
        return f"Try again {date} is an invalid date"
    elif first > 30 and second == 11:
        return f"Try again {date} is an invalid date"
    elif first == 1 and second > 31:
        return f"Try again {date} is an invalid date"
    elif first == 3 and second > 31:
        return f"Try again {date} is an invalid date"
    elif first == 5 and second > 31:
        return f"Try again {date} is an invalid date"
    elif first == 7 and second > 31:
        return f"Try again {date} is an invalid date"
    elif first == 8 and second > 31:
        return f"Try again {date} is an invalid date"
    elif first == 10 and second > 31:
        return f"Try again {date} is an invalid date"
    elif first == 12 and second > 31:
        return f"Try again {date} is an invalid date"
    elif first > 31 and second == 1:
        return f"Try again {date} is an invalid date"
    elif first > 31 and second == 3:
        return f"Try again {date} is an invalid date"
    elif first > 31 and second == 5:
        return f"Try again {date} is an invalid date"
    elif first > 31 and second == 7:
        return f"Try again {date} is an invalid date"
    elif first > 31 and second == 8:
        return f"Try again {date} is an invalid date"
    elif first > 31 and second == 10:
        return f"Try again {date} is an invalid date"
    elif first > 31 and second == 12:
        return f"Try again {date} is an invalid date" 
    elif first <= 12 and second <= 12:
        return f"{date} Is an ambigous date"
    else:
       return "Is non-ambigous"

print(ambiguous_date("05.0.2021"))