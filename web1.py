import requests
from bs4 import BeautifulSoup
import csv

# Create and open a CSV file in write mode
with open('scraped_books.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Rating'])

    for i in range(1, 6):
        url = f'https://books.toscrape.com/catalogue/page-{i}.html'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            books = soup.find_all('article', class_='product_pod')

            for book in books:
                title = book.h3.a.attrs['title']
                price = book.find('p', class_='price_color').text
                rating = book.find('p', class_='star-rating')['class'][1]
                writer.writerow([title, price, rating.capitalize()])
        else:
            print(f"Failed to retrieve the page {i}. Status code: {response.status_code}\n")

print("Data successfully exported to scraped_books.csv")



