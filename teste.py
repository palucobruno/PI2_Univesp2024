import requests
import pandas as pd

from IPython.display import display

api_key = "9b26662979198e5598352c16c9ac8893"

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()