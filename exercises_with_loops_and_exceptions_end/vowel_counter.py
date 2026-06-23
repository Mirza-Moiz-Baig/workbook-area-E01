word = input("Enter a word for us to count vowels: ")
counter = 0
for each_character in word: # loops run on strings similar to lists/tuples
    print(each_character)
    if each_character.upper() in "AEIOU":
        counter += 1

print(f"There are {counter} vowels in {word}")