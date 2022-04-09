import random

from source_data import user_name, favorite_movie


print(user_name[2])
print(favorite_movie[2])

for count in range(100):
    movie = random.randint(0, len(favorite_movie) -1)
    print(favorite_movie[movie])
