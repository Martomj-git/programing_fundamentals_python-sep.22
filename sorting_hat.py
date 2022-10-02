name = input()
chars = 0
lord = False
while name != 'Welcome!':
    chars = (len(name))
    if name == 'Voldemort':
        lord = True
        print('You must not speak of that name!')
        break
    if chars < 5:
        print(f'{name} goes to Gryffindor.')
    elif chars == 5:
        print(f'{name} goes to Slytherin.')
    elif chars == 6:
        print(f'{name} goes to Ravenclaw.')
    elif chars > 6:
        print(f'{name} goes to Hufflepuff.')
    name = input()
if not lord:
    print('Welcome to Hogwarts.')