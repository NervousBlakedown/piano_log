# Piano Log Reference.
# Add remainder for odd-number measure input to end of loop, count it as normal.
# Get whole total (append to blank list?)
# If measure total smaller than phase number, skip it.
print("\n")
measure_total = int(input("Thank you for using Blake's music memorization aid! \nEnter the total number of measures in your piece of music, then hit the return key: "))
timer_total = int(input("Enter the number of minutes you will spend on each small section, then hit the return key: "))

print("Phase I: 4-measure sections")
def music_measures_group_one(): # start, stop, step (AKA interval; step keeps alliteration game going strong.)
    for i in range(1, measure_total, 4): # last number should be one less than range interval.
        print((i), "-", i + 3)

        if i > measure_total:
            break
        else:
            continue

        if measure_total % 2 != 0: # even numbers modulo 2 return 0, odd numbers modulo 2 return 1.
            print((i), "-", i - 1)
        else:
            print(None)

    print("\n")

    measure_group_count = list(range(1, measure_total, 4))
    last_group = measure_group_count[-1]
    measure_index = measure_group_count.index(last_group)
    final_measure_group_count = measure_index + 1
    print(str(final_measure_group_count) + " sections total")
music_measures_group_one() # call the function; parentheses necessary.

measure_group_count = list(range(1, measure_total, 4))
last_group = measure_group_count[-1]
measure_index = measure_group_count.index(last_group)
final_measure_group_count = measure_index + 1

minutes_spent = timer_total * final_measure_group_count
hours_spent = (timer_total * final_measure_group_count) / 60
rounded_minutes = round(minutes_spent, 1)
rounded_hours = round(hours_spent, 2)

print("Estimated " + str(rounded_hours) + " hours/" + str(rounded_minutes) + " minutes to memorize Phase 1")
print("\n")


print("Phase 2: 8-measure sections")
def music_measures_group_two():
    for i in range(1, measure_total, 8):
        print((i), "-", i + 7)

        if i > measure_total:
            break
        else:
            continue

        if measure_total % 2 != 0:
            print((i), "-", i - 1)
        else:
            print(None)
    print("\n")

    measure_group_count = list(range(1, measure_total, 8))
    last_group = measure_group_count[-1]
    measure_index = measure_group_count.index(last_group)
    final_measure_group_count = measure_index + 1
    print(str(final_measure_group_count) + " sections total")
music_measures_group_two()

measure_group_count = list(range(1, measure_total, 8))
last_group = measure_group_count[-1]
measure_index = measure_group_count.index(last_group)
final_measure_group_count = measure_index + 1

minutes_spent = timer_total * final_measure_group_count
hours_spent = (timer_total * final_measure_group_count) / 60

rounded_minutes = round(minutes_spent, 1)
rounded_hours = round(hours_spent, 2)

print("Estimated " + str(rounded_hours) + " hours/" + str(rounded_minutes) + " minutes to memorize Phase 2")
print("\n")


print("Phase 3: 16-measure sections")
def music_measures_group_three():
    for i in range(1, measure_total, 16):
        print((i), "-", i + 15)

        if i > measure_total:
            break
        else:
            continue

        if measure_total % 2 != 0:
            print((i), "-", i - 1)
        else:
            print(None)
    print("\n")

    measure_group_count = list(range(1, measure_total, 16))
    last_group = measure_group_count[-1]
    measure_index = measure_group_count.index(last_group)
    final_measure_group_count = measure_index + 1
    print(str(final_measure_group_count) + " sections total")
music_measures_group_three()

measure_group_count = list(range(1, measure_total, 16))
last_group = measure_group_count[-1]
measure_index = measure_group_count.index(last_group)
final_measure_group_count = measure_index + 1

minutes_spent = timer_total * final_measure_group_count
hours_spent = (timer_total * final_measure_group_count) / 60

rounded_minutes = round(minutes_spent, 1)
rounded_hours = round(hours_spent, 2)

print("Estimated " + str(rounded_hours) + " hours/" + str(rounded_minutes) + " minutes to memorize Phase 3")
print("\n")


print("Phase 4: 32-measure sections")
def music_measures_group_four():
    for i in range(1, measure_total, 32):
        print((i), "-", i + 31)

        if i > measure_total:
            break
        else:
            continue

        if measure_total % 2 != 0:
            print((i), "-", i - 1)
        else:
            print(None)
    print("\n")

    measure_group_count = list(range(1, measure_total, 32))
    last_group = measure_group_count[-1]
    measure_index = measure_group_count.index(last_group)
    final_measure_group_count = measure_index + 1
    print(str(final_measure_group_count) + " sections total")
music_measures_group_four()

measure_group_count = list(range(1, measure_total, 32))
last_group = measure_group_count[-1]
measure_index = measure_group_count.index(last_group)
final_measure_group_count = measure_index + 1

minutes_spent = timer_total * final_measure_group_count
hours_spent = (timer_total * final_measure_group_count) / 60

rounded_minutes = round(minutes_spent, 1)
rounded_hours = round(hours_spent, 2)

print("Estimated " + str(rounded_hours) + " hours/" + str(rounded_minutes) + " minutes to memorize Phase 4")
print("\n")

print("Phase 5: 64-measure sections")
def music_measures_group_five():
    for i in range(1, measure_total, 64):
        print((i), "-", i + 63)

        if i > measure_total:
            break
        else:
            continue

        if measure_total % 2 != 0:
            print((i), "-", i - 1)
        else:
            print(None)
    print("\n")

    measure_group_count = list(range(1, measure_total, 64))
    last_group = measure_group_count[-1]
    measure_index = measure_group_count.index(last_group)
    final_measure_group_count = measure_index + 1
    print(str(final_measure_group_count) + " sections total")
music_measures_group_five()

measure_group_count = list(range(1, measure_total, 64))
last_group = measure_group_count[-1]
measure_index = measure_group_count.index(last_group)
final_measure_group_count = measure_index + 1

minutes_spent = timer_total * final_measure_group_count
hours_spent = (timer_total * final_measure_group_count) / 60

rounded_minutes = round(minutes_spent, 1)
rounded_hours = round(hours_spent, 2)

print("Estimated " + str(rounded_hours) + " hours/" + str(rounded_minutes) + " minutes to memorize Phase 5")
print("\n")

print("Phase 6: 128-measure sections")
def music_measures_group_six():
    for i in range(1, measure_total, 128):
        print((i), "-", i + 127)

        if i > measure_total:
            break
        else:
            continue

        if measure_total % 2 != 0:
            print((i), "-", i - 1)
        else:
            print(None)
    print("\n")

    measure_group_count = list(range(1, measure_total, 128))
    last_group = measure_group_count[-1]
    measure_index = measure_group_count.index(last_group)
    final_measure_group_count = measure_index + 1
    print(str(final_measure_group_count) + " sections total")
music_measures_group_six()

measure_group_count = list(range(1, measure_total, 128))
last_group = measure_group_count[-1]
measure_index = measure_group_count.index(last_group)
final_measure_group_count = measure_index + 1

minutes_spent = timer_total * final_measure_group_count
hours_spent = (timer_total * final_measure_group_count) / 60

rounded_minutes = round(minutes_spent, 1)
rounded_hours = round(hours_spent, 2)

print("Estimated " + str(rounded_hours) + " hours/" + str(rounded_minutes) + " minutes, to memorize Phase 6")
print("\n")

biggest_total = rounded_minutes
biggest_total_hours = rounded_minutes / 60

rounded_biggest_total = round(biggest_total, 1)
rounded_biggest_total_hours = round(biggest_total_hours, 2)

print("Total time spent on piece: " + str(rounded_biggest_total_hours) + " hours/" + str(rounded_biggest_total) + " minutes if you stick to the plan.  Happy practicing!")
