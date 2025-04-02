import requests
from bs4 import BeautifulSoup

def get_sports_news():
    espn_url = "https://www.espn.com/"
    bbc_url = "https://www.bbc.com/sport"
    
    espn_response = requests.get(espn_url)
    bbc_response = requests.get(bbc_url)
    
    espn_soup = BeautifulSoup(espn_response.content, "html.parser")
    bbc_soup = BeautifulSoup(bbc_response.content, "html.parser")
    
    espn_headlines = espn_soup.find_all("h1", class_="headline")
    bbc_headlines = bbc_soup.find_all("h3", class_="gs-c-promo-heading__title")
    
    espn_news = [headline.text for headline in espn_headlines]
    bbc_news = [headline.text for headline in bbc_headlines]
    
    return espn_news + bbc_news

def update_website(news):
    with open("sports_news.html", "w") as file:
        file.write("<html><body><h1>Sports News</h1><ul>")
        for item in news:
            file.write(f"<li>{item}</li>")
        file.write("</ul></body></html>")

if __name__ == "__main__":
    news = get_sports_news()
    update_website(news)