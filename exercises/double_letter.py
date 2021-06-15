""" 

Analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

Sample Inputs:

hello -> True
nono -> False
sunday -> False
racecar -> False

"""

def double_letter(wd):
	letters = {}
	for char in wd:
		if char not in letters:
			letters[char] = 0
		letters[char] += 1

	#filter out letter counts equal to 1
	letter_counts = filter(lambda k: k[1] != 1, letters.items())
	for letter, count in letter_counts:
		if letter * 2 in wd:
			return True 
	return False 


def double_letters2(string):
    x = 0
    while x < len(string) - 1:  
        if string[x] == string[x+1]:
            return True         
        x = x+1
    return False

def double_letter_w_range(string):
    for x in range(len(string)):  
        if string[x] == string[x+1]:
            return True 
    return False

def find_double_letters3(word):
    return len([letter for letter in word if letter*2 in word]) >= 1



if __name__ == '__main__':
	print(double_letter("hello"))
	print(double_letter("helo"))
	print(double_letter("nono"))