import re

with open('getnum.txt','r') as get_file:
    read_file = get_file.read()
# old solution
# x = re.findall('[0-9]+',read_file)
# sum_num = 0
# for i in x:
#     sum_num += int(i)
# list comprehension solutions
a = sum([int(i) for i in re.findall('[0-9]+',read_file)])
print(a)
