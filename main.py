import random
import requests

url = 'https://type.fit/api/quotes'
input = input("Input author's name: ")
if requests.get(url).status_code == 200:
    print(f"{input} said: ")
    data = requests.get(url).json()
    rand_quote = random.choice(data)
    print(rand_quote)
    print(f"{rand_quote['text']}")

else:
    print("failed")
