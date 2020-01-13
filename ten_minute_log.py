# Piano Log Reference.
# Memorization in ten-minute intervals.
# Print measure groupings for Spreadsheet (four measures, eight measures, etc.).

def music_measures_group_one(): # parameter should return measure number total.
    for i in range(1, 201, 4): # start, stop, step (AKA interval; step keeps alliteration game going strong.)
        print((i), "-", i + 3) # last number should be one less than range interval.
music_measures_group_one() # call the function; parentheses necessary.
print("\n") # line break!


def music_measures_group_two():
    for i in range(1, 201, 8):
        print((i), "-", i + 7)
music_measures_group_two()
print("\n")


def music_measures_group_three():
    for i in range(1, 201, 16):
        print((i), "-", i + 15)
music_measures_group_three()
print("\n")


def music_measures_group_four():
    for i in range(1, 201, 32):
        print((i), "-", i + 31)
music_measures_group_four()
print("\n")


def music_measures_group_five():
    for i in range(1, 201, 64):
        print((i), "-", i + 63)
music_measures_group_five()
print("\n")


def music_measures_group_six():
    for i in range(1, 201, 128):
        print((i), "-", i + 127)
music_measures_group_six()
