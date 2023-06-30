
def print_upper_words(names, letters):
    """prints all names in list in all upper case IF their name starts with e"""
    for name in names:
        for letter in letters:
            if name[0] == letter or name[0] == letter.swapcase():
                print(name.upper())

print_upper_words(['Nancy', 'Hayley','Eli', 'Dorion', 'DJ', 'Lincoln', 'Elvis'], ['n','e','d'])