
from itertools import product
from pprint import pprint 
"""

Dates can be written differently depending where you are in the world 05.05.2021 (the fifth of may 2021) 03.05.2021 (the third of may 2021 -> Europe, the 5th of march 2021 -> US) 05.03.2021 (the fifth of march 2021 -> Europe, the 3th of may 2021 -> US)

Sample Inputs (strings '05.05.2021'):

05.05.2021 -> non-ambiguous
03.05.2021 -> ambiguous
05.03.2021 -> ambiguous
Write a function that detects if a date, written in the format NN.NN.NNNN where n is a digit [0-9] is ambiguous
save all the dates of the year that are ambiguous and print to user
Extra: write a function that converts the format NN.NN.NNNN to a date such as "the 5th of May, 2021" (HINT: Use string formatting, and lists of strings)


January - 31 days.
February - 28 days in a common year and 29 days in leap years.
March - 31 days.
April - 30 days.
May - 31 days.
June - 30 days.
July - 31 days.
August - 31 days.
	


"""


# a lot of cases for this one.

"""
def is_valid_date(date):
	#make sure it's a valid date 
	if any(num > 31 for num in dd_mm_as_ints):
		return False

	#12 + 31 = 43;
	if sum(dd_mm_as_ints) > 43:
		return  False

	#there are a a lot of cases....
	# watch out for feburary which has 28 days (29 for a leap year but we are gonna ignore that)
	if 2 in dd_mm_as_ints and sum(dd_mm_as_ints) < 31:
		return False 

	return True 
"""


def date_checker(date_to_check):
	date_parts = date_to_check.split('.')
	dd_mm_as_ints = list(map(int, date_parts[:2]))

	"""
	if not is_valid_date(dd_mm_as_ints):
		return "not a valid date"
	"""

	#covers the case where dd==mm  i.e. 05.05.2021
	if date_parts[0] == date_parts[1]:
	   return "non-ambiguous"

	#first cast the day and month into ints
	#if they are less than 12, they are ambiguous
	#more than twelve, there is only one valid date it could be
	# i.e. 13.12.2021 could only be a european date ; thus non-ambiguous
	# i.e. 12.13.2021 could only be an american date; thus non-ambiguous
	elif all(part < 13 for part in dd_mm_as_ints):
		return "ambiguous"
	return "non-ambiguous"

#functional one line solution
def generate_all_dates_one_line(start='01.01.2021', end='12.12.2021'):
	return [f"{fst}.{snd}.2021" for fst,snd in product(range(1,32), range(1,13))]


#functional solution
def generate_all_dates(start='01.01.2021', end='12.12.2021'):

	all_possible_dates = list(product(range(1,32), range(1,13)))
	dates_as_strings = [f"{fst}.{snd}.2021" for fst,snd in all_possible_dates]
	return dates_as_strings 

#iterative solution
def generate_all_dates_iterative(start='01.01.2021', end='12.12.2021'):
	number_of_days_in_month = 31
	number_of_months_in_year = 12
	# number of months in year = 12
	dates_as_strings = []

	for day in range(1,number_of_days_in_month + 1):
		for month in range(1,number_of_months_in_year + 1):
			dates_as_strings.append(f"{day}.{month}.2021")
	return dates_as_strings 



def get_all_ambiguous_dates():

	"""
	For loop version without list comp: 
	save_the_dates = []
	for date in generate_all_dates():
		if date_checker(date) == 'ambiguous':
			save_the_dates.append(date)

	"""
	return [date for date in generate_all_dates() if date_checker(date) == 'ambiguous']

def print_as_human_readable(day, month, year):
	
	month_names = ['January', 'February', 'March', 'April','May', 'June', 'July', 'August','September', 'October','November','December']	 
	months = { idx + 1: mon for idx,mon in enumerate(month_names) }
	day_str = str()
	month_str = str()
	day = int(day)
	month = int(month)

	#1st, 2nd, 3rd, 4th, 5th, 6th
	last_digit = int(str(day)[-1])
	if day == 1:
	    day_str = str(day) + 'st'
	elif day in range(4,21) or day in range(25,30):
		day_str = str(day) + 'th'	
	elif last_digit == 2:
		day_str = str(day) + 'nd'	
	elif last_digit == 3:
		day_str = str(day) + 'rd'

	
	return f"the {day_str} of {months[int(month)]}, {year}"


if __name__ == '__main__':
	print(date_checker('05.05.2021'))
	print(date_checker('03.05.2021'))
	print(date_checker('05.03.2021'))
	print(date_checker('12.12.2021'))
	print(date_checker('32.03.2021'))
	pprint(get_all_ambiguous_dates())

	print(print_as_human_readable('12','12','2021'))
	print(print_as_human_readable('25','12','2021'))
    all_dates = generate_all_dates()
    print(all_dates)
