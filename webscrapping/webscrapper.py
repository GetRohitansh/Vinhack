from bs4 import BeautifulSoup
import requests

city = input("Enter City: ")
dish = input("Enter dish: ")
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
url = 'https://www.zomato.com/{cityName}/restaurants?q={dishName}'.format(cityName = city, dishName = dish)
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')
restaurant_cards = soup.find_all("div", class_="search-card")
for card in restaurant_cards:
    name = card.find('a', class_='result-title hover_feedback zred bold ln24 fontsize0').text
    address = card.find('div', class_='col-m-16 search-result-address grey-text nowrap ln22').text
    price_range = card.find('span', class_='col-s-11 col-m-12 pl0').text
    print(name, address, price_range)
    print("--------------------------")

print(url)