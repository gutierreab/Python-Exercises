# How to print a 'Welcome' phrase in Python, using 'format' and colored font.

# Font: Color Blue, underlined in White.

name = input('Enter your name: ')

print('Welcome, \033[4;36;107m{}\033[m!'.format(name))

# Created by Amanda Borges Gutierre, on August 4th, 2022.
