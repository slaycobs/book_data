# %%
# Imports
from requests import get, Response
from bs4 import BeautifulSoup
from pprint import pprint
# %%
# Collect all URLs to genres 
years = [i for i in range(2011, 2024)]
best_books_url = "https://www.goodreads.com/choiceawards/{}"
for year in years:
    url = best_books_url.format(f"best-books-{year}")
    resp = get(url)
    if resp.status_code != 200:
        assert(False, f"Unexpected status code for URL: {url}, code: {resp.status_code}")
    page = BeautifulSoup(resp.content, features="html.parser")
    genre_urls = []
    for tag in page.find_all("a"):
        href = tag.get("href")
        if href != None and "choiceawards" in href:
            genre_urls.append(best_books_url.format(href))
    pprint(genre_urls)
    break

# %%


# %%