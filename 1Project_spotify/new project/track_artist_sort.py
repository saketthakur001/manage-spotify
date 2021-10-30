# # artists = open('artists.csv', 'r+', encoding='utf-8')
# tracks = open('tracks.csv', 'r+', encoding='utf-8')

# tracks = [i for i in tracks]

# times = sorted([int(i.split('===')[1].split('"\n')[0]) for i in tracks])


# t = open('sorted_tracks.csv', 'w', encoding='utf-8')
# for num in times[::-1]:
#     for i in tracks:
#         print(int(i.split('===')[1].split('"\n')[0]))
#         # if int(i.split('===')[1].split('"\n')[0]) == num:
#         #     t.write(i[:-2]+'\n')

import pandas as pd
# Read in your .csv files as dataframes
# df is a common standard for naming a dataframe. You can
# name them something more descriptive as well.
# Using a descriptive name is helpful when you are dealing
# with multiple .csv files.
df = pd.read_csv(r"C:\Users\saket\Desktop\don't delete 'em\python files\.movies\IMDb movies.csv")
# the .sort_values method returns a new dataframe, so make sure to
# assign this to a new variable.
sorted_df = df.sort_values(by=["votes"], ascending=False)
# Index=False is a flag that tells pandas not to write
# the index of each row to a new column. If you'd like
# your rows to be numbered explicitly, leave this as
# the default, True
sorted_df.to_csv('Movies_sorted_by_votes.csv', index=False)
