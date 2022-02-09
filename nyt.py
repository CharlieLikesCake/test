import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
API_KEY = os.getenv("API_KEY")
def article_search(){
    params = {
    "q": "election",
    "api-key": API_KEY
 }
}
response = requests.get(
    BASE_URL,
    params=params,
)
headlines =[]
snippets =[]
response_json = response.json()


articles = response_json["response"]["docs"]
for article in articles:
    headlines.append(article["headline"]["main"])
    snippets.append(article["snippet"])

return headlines, snippets

