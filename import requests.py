import requests

def search_gifs(search_query):
    api_key = 'BYAObLWHDa3LwtWMgg2Jat3uhEu000Yh'
    url = f'https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_query}&limit=5'
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        for gif in data['data']:
            gif_url = gif['images']['original']['url']
            print(gif_url)
    else:
        print('Error occurred while searching for GIFs.')

search_word = input("Enter a search word: ")
search_gifs(search_word)