command = input()
coffees_needed = 0
while command != 'END':
    if command == 'coding' or command == 'cat' \
            or command == 'dog' or command == 'movie':
        coffees_needed += 1
    elif command == 'CODING' or command == 'CAT' \
            or command == 'DOG' or command == 'MOVIE':
        coffees_needed += 2
    command = input()
if coffees_needed > 5:
    print('You need extra sleep')
else:
    print(coffees_needed)




