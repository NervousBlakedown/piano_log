# Music Log.
# Imports
import pandas as pd

def get_practice_time_for_group(group_size, minutes_per_group, measures):
    """organize practice time needed to memorize music."""
    total_time = 0
    df_data = []
    for group_start in range(1, measures + 1, group_size):
        group_end = min(group_start + group_size - 1, measures)
        group_time = minutes_per_group
        total_time += group_time
        df_data.append({
            "Measure Grouping": f"measures {group_start} to {group_end}",
            "Duration": f"{group_time} minutes"
        })
    return total_time, df_data

def practice_time(measures: int, minutes_per_group: int, composer: str = None, piece: str = None, group_sizes=[4, 8, 16, 32, 64]):
    if not composer:
        composer = input("Please enter the composer name: ")
    if not piece:
        piece = input("Please enter the piece name: ")

    total_time = 0
    df_data = []

    for group_size in group_sizes + [measures]:
        group_time, group_data = get_practice_time_for_group(group_size, minutes_per_group, measures)
        total_time += group_time
        for data in group_data:
            data.update({"Composer": composer, "Piece": piece})
            df_data.append(data)

    hours = total_time / 60
    print(f"Total practice time: {total_time} minutes ({hours:.2f} hours)")

    df = pd.DataFrame(df_data)
    df["Total Minutes Practiced"] = total_time
    df["Total Practice Time"] = f"{total_time} minutes ({hours:.2f} hours)"
    
    print("\nPractice Summary:")
    print(df)

    # Optional: Plotting
    # df.plot(kind='bar', x='Measure Grouping', y='Duration')
    # plt.show()

    return hours
