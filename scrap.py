from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


def get_rating(star_element):
    """
    Converts rating class like:
    'star-rating Three' -> 3
    """
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    classes = star_element.get_attribute("class").split()
    for c in classes:
        if c in rating_map:
            return rating_map[c]
    return None


driver = webdriver.Chrome()

# Website (safe practice site)
url = "https://books.toscrape.com/catalogue/page-1.html"
driver.get(url)

books_data = []
page = 1

while True:
    print(f"Scraping Page {page}...")

    time.sleep(2)  # small delay to load page

    # Find all books on page
    books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

    for book in books:
        try:
            title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
        except:
            title = "N/A"

        try:
            price = book.find_element(By.CLASS_NAME, "price_color").text
        except:
            price = "N/A"

        try:
            availability = book.find_element(By.CLASS_NAME, "availability").text.strip()
        except:
            availability = "N/A"

        try:
            rating_element = book.find_element(By.CLASS_NAME, "star-rating")
            rating = get_rating(rating_element)
        except:
            rating = "N/A"

        try:
            link = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            link = "N/A"

        books_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Link": link
        })

    # Check if "next" button exists
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        next_link = next_button.get_attribute("href")

        driver.get(next_link)
        page += 1

    except:
        print("No more pages. Scraping finished!")
        break


driver.quit()

# -------- Save Output --------
df = pd.DataFrame(books_data)

df.to_csv("books.csv", index=False)
df.to_json("books.json", orient="records", indent=4)

print("\nScraping Done!")
print("Saved: books.csv and books.json")
print("Total books scraped:", len(df))
