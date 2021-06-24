



phrase = 'Python is a great programming language'
#python converts strings in character arrays
#str.toCharArray()
for i in range(len(phrase)):
    print(phrase[i], end=',')   # <==== Indexing used to access the elements 
print()

a_lst = ['A','B','C','D','E','F']
a_tpl = ('oranges','apples','pears','grapes','kiwi')

for i in range(len(a_lst)):
    print(a_lst[i], end=',')   # <==== Indexing used to access the elements 
print()                                           
for i in range(len(a_tpl)):
    print(a_tpl[i], end=',')   # <==== Indexing used to access the elements
print()

a_lst = range(100,105)
a_tpl = ('oranges','apples','pears','grapes','kiwi')
a_tpl2 = ('oranges','apples','pears','grapes','kiwi', 'grapefruit')
#zip both lists have to be the same length
a_dict = zip(a_lst,a_tpl)
a_dict2 = zip(a_lst,a_tpl2)
print(list(a_dict))
print(list(a_dict2))
print(type(a_dict))
a_dict = dict(a_dict)
print('='*35)
print(a_dict)
print(type(a_dict))

#just make sure they are the same length
a_lst = range(100,105)
a_tpl = ('oranges','apples','pears','grapes','kiwi')
a_dict = dict(zip(a_lst,a_tpl))

print(a_dict[100])
"""iterate"""
for i in range(100,100+len(a_dict)):
    print(i,a_dict[i], end=',')   # <==== Indexing used to access the keys 

phrase = 'Python is a great programming language'      # <=== String
a_lst = ['A','B','C','D','E','F']                      # <=== list
a_tpl = ('oranges','apples','pears','grapes','kiwi')   # <=== tuple
a_dict = {'011X':'4K TV',
         '023B':'Air fryer',
         '99AB': 'Instapot'}                           # <=== dictionary

print('String '+'*'*15)
for i in phrase:   # <=== String
    print(i, end = ',')
print()
#
print('List '+'*'*15)
for i in a_lst:   # <=== list
    print(i, end = ',')
print()
#
print('Tuple '+'*'*15)
for i in a_tpl:   # <=== Tuple
    print(i, end = ',')
print()
#
print('Dictionary '+'*'*15)
for k,v in a_dict.items():   # <=== dictionary
    print(f'They key is {k}, The value is {v}')
print()

phrase = 'Python is a great programming language'      # <=== String
a_lst = ['A','B','C','D','E','F']                      # <=== list
a_tpl = ('oranges','apples','pears','grapes','kiwi')   # <=== tuple
a_dict = {'011X':'4K TV',
         '023B':'Air fryer',
         '99AB': 'Instapot'}                           # <=== dictionary

print('String '+'*'*15)
for i,char in enumerate(phrase):   # <=== String
    print(f'The character at index {i} is {char}')
print()

for index, char in enumerate(phrase):
    if char == 'P' and index == 0:
        print("string starts with P")
#
print('List '+'*'*15)
for i,item in enumerate(a_lst):   # <=== list
    print(f'The character at index {i} is {item}')
print()
#
print('Tuple '+'*'*15)
for i,item in enumerate(a_tpl):   # <=== Tuple
    print(f'The item at index {i} is {item}')
print()
#
print('Dictionary '+'*'*15)
for i,val in enumerate(a_dict):   # <=== dictionary ****
    print(f'The index is {i}, The key is {val}')
print()


#chapters = ['Chapter 1','Chapter 2','Chapter 3','Chapter 4','Chapter 5']
subject = ['Declaring variables','Data structures','Iteration','List comprehension',
    'Object Oriented programming']

chapters2 = ['Chapter' for i in range(5)]
print(chapters2)


for i,item in enumerate(chapters2):
    print(f'{item} {i + 1}-{subject[i]}')
            
#problem: add back chapter numbers

from itertools import repeat
print(list(repeat("Chapter",5)))




import string

letters = string.ascii_letters

#print out all the letters and even indicies 
#print out all the letters at odd indicies 
#using enumerate 

for index, char in enumerate(letters):
    if index % 2 == 0:
        print(f"char {char} is at an even index")
    else:
        print(f"char {char} is at an odd index")
        
letters_at_even_positions = [char for index, char in enumerate(letters) if index % 2 == 0 ]
print(letters_at_even_positions)
letters_at_odd_positions = [char for index, char in enumerate(letters) if index % 2 == 1 ]

print(even)



