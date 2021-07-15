months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}
def dateNum_converter(x):
    x = x.split(".")
    x[0] = int(x[0])
    x[1] = int(x[1])
    x[2] = int(x[2])
    if x[0] == x[1] and x[0]<13:
        return (f"The {x[0]}th of {months[x[1]]} in the year {x[2]}")
    elif x[0] in range(1,13) and x[1] in range(1,13):
        return ((f"The {x[1]}th of {months[x[0]]}"), (f"the {x[0]}th of {months[x[1]]} in the year {x[2]}")) 
    elif (x[0] in range(1, 13) and x[1] in range (13, 32)):
        return (f"The {x[1]}th of {months[x[0]]} in the year {x[2]}")
    elif (x[1] in range(1, 13)) and (x[0] in range (13, 32)):
        return (f"The {x[0]}th of {months[x[1]]} in the year {x[2]}")
    else:
        return ("Oops, invalid day or month")
        

def date_or_not(x):
    short = [2, 4, 6, 9, 12]
    amb = range (1, 13)
    n = x.split(".")
    n[0] = int(n[0])
    n[1] = int(n[1])
    n[2] = int(n[2])
    if len(n)>3 or (n[0] + n[1]) > 43:
        return print("Oops, something went wrong. Please enter the date again")
    for i in range(0,2):
        if n[i] <= 0 or n[i] > 31:
            return print(f"Impossible date, {n[i]}th day or month does not exist")
    if (n[0] == 29 and n[1] == 2)  or (n[0] == 2 and n[1] == 29):
        if ((n[2]%4 == 0) and (n[2]%100 != 0)) or ((n[2]%4 == 0) and (n[2]%100 == 0) and (n[2]%400 == 0)):
            return print(f"The 29th day of {months[2]} in the year {n[2]} which is a leap year, is a valid date")
        else:
            return print(f"{dateNum_converter(x)} is an impossible date, the year {n[2]} is not a leap year")
    elif n[0] == n[1] and n[0] < 13:
        return print(f"{dateNum_converter(x)} is valid and unambiguous date")
    elif n[0] == n[1] and n[0] > 12:
        return print(dateNum_converter(x))
    elif n[0] in short and n[1] == 31:
        return print(f"Impossible date, {dateNum_converter(x)} does not exist")
    elif n[0] in amb and n[1] in amb:
        return print(f"{x} is a valid but ambiguous, can either be {dateNum_converter(x)[0]} or {dateNum_converter(x)[1]}")
    else:
        return print(f"{dateNum_converter(x)} is valid and unambiguous")