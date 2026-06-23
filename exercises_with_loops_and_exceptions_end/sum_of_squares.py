my_square = int(input("Enter a number to sum the squares: "))
total = 0
for num in range(my_square):
    total += ((num+1) ** 2)

print(F"The sum of squares is {total}")
   