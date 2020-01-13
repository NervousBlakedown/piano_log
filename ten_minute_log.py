# Memorization in ten-minute intervals.

def music_measures_group_one(): 
    for i in range(1, 201, 4): # stop number = total number of measures
        print((i), "-", i + 3) 
music_measures_group_one() 
print("\n") 


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
