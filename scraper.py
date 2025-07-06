import requests
import sys
import datetime
from bs4 import BeautifulSoup # type: ignore

class Article:
    def __init__(self, blog: str):
        self.blog = blog
        self.title = blog.find('a', class_='entry-title-link').get_text() # type: ignore
        datetime_string = blog.find('time', class_='entry-time').get('datetime') # type: ignore
        self.datetime = datetime.datetime.fromisoformat(datetime_string)
        self.date = self.datetime.strftime("%b %d, %Y")

    def __str__(self):
        return f"The article is titled \"{self.title}.\" It was published on {self.date}."


url = "https://pixelford.com/blog/"
try:
    response = requests.get(url, headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'})
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    articles_soup = soup.find_all('article', class_='type-post')
    # This creates articles objects
    articles = list(map(lambda article: Article(article), articles_soup))
    for article in articles:
        print(article)


    # These work, but are just messy and I don't like them.
    # blog_titles = list(map(lambda article: article.find('a', class_='entry-title-link').get_text(), blogs))
    # blog_datetime_strings = list(map(lambda article: article.find(class_='entry-time').get('datetime'), blogs))
    # blog_times = list(map(lambda datetime_string: ( (datetime.datetime.fromisoformat(datetime_string)).strftime("%B %d, %Y") ), blog_datetime_strings))
    
            
except requests.exceptions.ConnectionError as e:
    print("Connection error. Please check your internet connection,", e)
    sys.exit()
except requests.exceptions.Timeout as e:
    print("Connection timed out. Please check your internet connection,", e)
    sys.exit()