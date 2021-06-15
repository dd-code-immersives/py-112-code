def get_ascii_sum(input_str='hello'):
	total = 0
	for ch in input_str:
		print(f"character {ch}, ascii value {ord(ch)}")
		total += ord(ch)
	return total

def get_ascii_sum2(input_str='hello'):
	total_chars = []
	for ch in input_str:
		print(f"character {ch}, ascii value {ord(ch)}")
		total_chars.append(ord(ch))
	return sum(total_chars)


def ascii_one_liner(input_str='hello'): return sum(ord(ch) for ch in input_str)


total = ascii_one_liner()
print(f"the ascii-total is {total}")
