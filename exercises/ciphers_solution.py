import string
import operator

def cesear_cipher(message):
	words = message.upper().split()
	letters = string.ascii_uppercase
	cipher_letters = [letters[i - 3] for i in range(len(letters))]
	cipher_map = dict(zip(letters, cipher_letters))
	cipher_words = []
	for word in words:
		cipher_word = "".join([cipher_map[letter] for letter in word])
		cipher_words.append(cipher_word)
	return " ".join(cipher_words)

def cesear_cipher_alt(message):
	words = message.upper().split()
	letters = string.ascii_uppercase
	cipher_letters = [letters[i - 3] for i in range(len(letters))]
	cipher_map = dict(zip(letters, cipher_letters))
	#map the dictionary onto each word
	cipher_words = ["".join(map(cipher_map.get, word)) for word in words]
	return " ".join(cipher_words)

def n_cipher(message,n=4,direction='right'):
	words = message.upper().split()
	letters = string.ascii_uppercase

	#change operator according to direction (-, left), (+, right)
	op = operator.sub if direction == 'left' else operator.add

	cipher_letters = [letters[op(i, (n - 1)) % len(letters)] for i in range(len(letters))]
	cipher_map = dict(zip(letters, cipher_letters))
	cipher_words = []
	for word in words:
		cipher_word = "".join([cipher_map[letter] for letter in word])
		cipher_words.append(cipher_word)
	return " ".join(cipher_words)

if __name__ == '__main__':
	print(cesear_cipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"))
	#print(n_cipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"))

