line_1 = ["⬜️", "️⬜️", "️⬜️"]
line_2 = ["⬜️", "️⬜️", "️⬜️"]
line_3 = ["⬜️", "️⬜️", "️⬜️"]

treasure_map = [line_1, line_2, line_3]

print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Hiding your treasure! X marks the spot**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

# user input
position = input('Where do you want to place it? A-C, 1-3 e.g. B3: ')
letter_position = position[0].lower()
abc_list = ['a', 'b', 'c']

# letter index
letter_index = abc_list.index(letter_position)

# number index
number_index = int(position[1]) - 1

# replace map with X
treasure_map[number_index][letter_index] = "X"

# print map
print(f"{line_1}\n{line_2}\n{line_3}")
