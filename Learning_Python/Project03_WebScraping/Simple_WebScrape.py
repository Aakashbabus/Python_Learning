import requests
from bs4 import BeautifulSoup

def simple_web_scraping(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and print specific elements from the webpage
        # For example, let's find all the links (anchor tags) on the page
        links = soup.find_all('a')
        for link in links:
            print(link.get('href'))
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)

if __name__ == "__main__":
    url = input("Enter the URL of the webpage to scrape: ")
    simple_web_scraping(url)
