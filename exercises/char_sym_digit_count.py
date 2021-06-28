import string 

def findDigitsCharsSymbols(inputString):
  charCount = 0
  digitCount = 0
  symbolCount = 0
  for char in inputString:
    char = char.strip()
    if char.islower() or char.isupper():  #if in string.ascii_letters
      charCount+=1
    elif char.isnumeric():
      digitCount+=1
    else:
      symbolCount+=1
      
  print("Chars = ", charCount, "Digits = ", digitCount, "Symbol = ", symbolCount)
      
inputString = "P@#yn26at^&i5ve"
print("total counts of chars, digits,and symbols \n")

findDigitsCharsSymbols(inputString)