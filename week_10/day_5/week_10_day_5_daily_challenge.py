#DAILY CHALLENGE

import time
import requests


def time_to_load(webpage):
    start = time.time()
    requests.get(webpage)
    end = time.time()
    delta = end - start
    return f'Time to load {webpage} : {delta} seconds'


print(time_to_load("https://www.google.com"))
print(time_to_load("https://www.ynet.com"))
print(time_to_load("https://www.imdb.com"))
print(time_to_load("https://www.sephoraberrebi.ai"))






