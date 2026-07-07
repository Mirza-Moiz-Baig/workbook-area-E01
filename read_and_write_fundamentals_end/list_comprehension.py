numbers = [1,2,3,4]
squares = [each_num * each_num for each_num in numbers]
print(squares)

lst = []
words = ['cat','dog','ant']
for word in words:
    lst.append(word.upper())

lst = [word.upper() for word in words]


clean_names = []

for name in names:
    clean_names.append(name.strip())

clean_names = [name.strip() for name in names]




names = [" Ali ", " Sara ", " Ahmed "]

clean_names = [name.strip() for name in names]
clean_names = []
for name in names:
    clean_names.append(name.strip())


print(clean_names)




clean_names = []

for name in names:
    if name.strip():
        clean_names.append(name.strip())

clean_names = [name.strip() for name in names if name.strip()]