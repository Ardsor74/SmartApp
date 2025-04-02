import requests
from bs4 import BeautifulSoup

def get_sports_news():
    url = "https://www.espn.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    headlines = soup.find_all("h1", class_="headline")
    return [headline.text for headline in headlines]

def update_website(news):
    with open("sports_news.html", "w") as file:
        file.write("<html><body><h1>Sports News</h1><ul>")
        for item in news:
            file.write(f"<li>{item}</li>")
        file.write("</ul></body></html>")

if __name__ == "__main__":
    news = get_sports_news()
    update_website(news)