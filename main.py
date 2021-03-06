import random
import time

import gspread

from source_data import user_name, favorite_movie

sa = gspread.service_account("credentials-sheets.json")
sh = sa.open("python-google")
# google sheet is at: https://docs.google.com/spreadsheets/d/1LFSmJ5kSsY_qlH8EypKOFTqb3NesCN-VRxufq9jdTSE/edit#gid=0

worksheet = sh.sheet1
worksheet.clear()

for num in range(1, 50):
    first_name = random.randint(0, len(user_name) - 1)
    last_name = random.randint(0, len(user_name) - 1)
    full_name = f"{user_name[first_name]} {user_name[last_name]}"
    movie = favorite_movie[random.randint(0, len(favorite_movie) - 1)]
    age = random.randint(10, 100)

    worksheet.update_cell(num, 1, full_name)
    worksheet.update_cell(num, 2, age)
    worksheet.update_cell(num, 3, movie)

    time.sleep(3)

"""
    Limit of 93 SEND commands per minute. Any more and it will error out.
    For three columns, this will be 31 rows.
"""