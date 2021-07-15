import os 

project_dir = 'C:\\temp\final_project\\'
os.chdir('/Users/andrewdoyle/Documents/code-immersives/py-112-code/exercises/')
files = os.listdir('.')
#print(files)

#list only python files. 
#py_files = os.listdir('*.py')
#print(py_files)

# listdir doesn't let us pass things like that, so we have to filter manually if we wanna use listdir 
py_files = [py_file for py_file in os.listdir('.') if py_file.endswith(".py")]

for file in os.listdir('.'):
    if file.endswith(".py"):
        print(file)

import os 
from glob import glob
file_path = "/Users/andrewdoyle/Documents/code-immersives/py-112-code/exercises/"
os.chdir(file_path)


# prints all files in working directory ending with .py
# for file in glob("*.py"):
#     print(file)

# finds one file with 
# print("=" * 36)    
# for file in glob('[0-9].py'):
#     print(file)
    
print("=" * 36)    
for file in glob('*[1-9][2-9][2-9][b-z]_.py'):
    print(file)

# 111_>.py
# 111_\*_.py
    
for file in glob('*.py'):
    print(file)