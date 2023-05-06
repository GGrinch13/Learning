import random
import requests

url = 'https://type.fit/api/quotes'
if requests.get(url).status_code == 200:
    data = requests.get(url).json()
    rand_quote = random.choice(data)
    print(f"{rand_quote['text']}")
    print(f"{rand_quote['author']}")

else:
    print("failed")
