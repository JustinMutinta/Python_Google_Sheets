import random
import gspread

from source_data import user_name, favorite_movie

sa = gspread.service_account("credentials-sheets.json")
sh = sa.open("python-google")

print(user_name[2])
print(favorite_movie[2])
"""
for count in range(100):
    first_name = random.randint(0, len(user_name) - 1)
    last_name = random.randint(0, len(user_name) - 1)
    movie = random.randint(0, len(favorite_movie) - 1)
    age = random.randint(10, 100)
    #print(favorite_movie[movie])
    print(f"{user_name[first_name]} {user_name[last_name]}, who is {age} years old, has a huge love for the movie {favorite_movie[movie]}")
"""