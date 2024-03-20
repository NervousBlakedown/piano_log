# Music Log.
# TODO: Jupyter Notebook check, export options

# Imports
import pandas as pd
import plotly.graph_objects as go

# Practice interations
def get_practice_time_for_group(group_size, minutes_per_group, measures, start_time=0):
    """Organize practice time needed to memorize music."""
    total_time = start_time
    df_data = []
    for group_start in range(1, measures + 1, group_size):
        group_end = min(group_start + group_size - 1, measures)
        group_time = minutes_per_group
        total_time += group_time
        df_data.append({
            "Measure Grouping": f"{group_start}-{group_end}",
            "Duration": f"{group_time} minutes",
            "Cumulative Practice Time": total_time  # Track cumulative time
        })
    return total_time, df_data

# User Practice Input
def practice_time():
    """Takes user input for personalized practice routine."""
    composer = input("Please enter the composer name: ")
    piece = input("Please enter the piece name: ")
    measures = int(input("Please enter the total number of measures in the piece: "))
    minutes_per_group = int(input("Please enter the number of minutes you will spend on each group of measures: "))

    group_sizes_input = input("Enter preferred group sizes separated by commas (e.g., 4,8,16,32): ")
    group_sizes = [int(size.strip()) for size in group_sizes_input.split(',')]

    total_time = 0
    df_data = []

    for group_size in group_sizes + [measures]:
        total_time, group_data = get_practice_time_for_group(group_size, minutes_per_group, measures, total_time)
        for data in group_data:
            df_data.append(data)

    df = pd.DataFrame(df_data)
    df["Cumulative Practice Time"] = df["Cumulative Practice Time"].apply(lambda x: f"{x} minutes ({x/60:.2f} hours)")

    # Identify rows where measure grouping starts over at 1
    color_flag = [True if row["Measure Grouping"].startswith("1-") else False for index, row in df.iterrows()]
    colors = ['lightblue' if flag else 'whitesmoke' for flag in color_flag]  # 'lightblue' for highlighted rows, 'whitesmoke' for others

    title_text = f"{composer} - {piece}<br><sub>Total practice time: {total_time} minutes ({total_time/60:.2f} hours)</sub>"

    fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns),
                    fill_color='lightgrey',  # Soft grey for header
                    align='left'),
        cells=dict(values=[df[col] for col in df.columns],
                   fill_color=[colors, colors, colors],  # Apply new colors for each column
                   align='left'))
    ])

    fig.update_layout(title=title_text)

    fig.show()

# Run app
if __name__ == '__main__':
    practice_time()
