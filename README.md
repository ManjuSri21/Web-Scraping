# 📚 Books Scraper - Selenium Web Scraping Project

A web scraping project using Selenium to extract book information from [books.toscrape.com](https://books.toscrape.com). This scraper demonstrates practical techniques for handling pagination, error handling, and data export.

## ✨ Features

- ✅ Scrapes books from multiple pages automatically
- ✅ Extracts: Title, Price, Rating, Availability, Link
- ✅ Handles pagination seamlessly
- ✅ Robust error handling with try-except blocks
- ✅ Saves data in **CSV** and **JSON** formats
- ✅ Real-time scraping progress display

## 📋 Requirements

- Python 3.7+
- Chrome browser
- ChromeDriver (must match your Chrome version)

## 🚀 Installation & Setup

### 1. Install Python Dependencies

```bash
pip install selenium pandas openpyxl
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### 2. Download ChromeDriver

1. Check your Chrome version: `Settings → About Google Chrome`
2. Download matching ChromeDriver from: [chromedriver.chromium.org](https://chromedriver.chromium.org)
3. **Option A:** Add to system PATH
4. **Option B:** Place in project folder and update path in script:

```python
driver = webdriver.Chrome("./chromedriver")  # If in same folder
```

### 3. Run the Scraper

```bash
python scrap.py
```

## 📊 Output

The script generates two files:

### **books.csv**
```
Title,Price,Rating,Availability,Link
Sapiens: A Brief History of Humankind,£54.23,3,In stock,catalogue/sapiens-a-brief-history-of-humankind_327/index.html
...
```

### **books.json**
```json
[
  {
    "Title": "Sapiens: A Brief History of Humankind",
    "Price": "£54.23",
    "Rating": 3,
    "Availability": "In stock",
    "Link": "catalogue/sapiens-a-brief-history-of-humankind_327/index.html"
  }
]
```

## 📖 How It Works

### 1. **Setup WebDriver**
```python
driver = webdriver.Chrome()  # Launches Chrome browser
```

### 2. **Navigate Website**
```python
driver.get("https://books.toscrape.com/catalogue/page-1.html")
```

### 3. **Extract Book Data**
```python
books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
```

### 4. **Parse Information**
- Title: `<h3><a title="Book Name">`
- Price: `.price_color` class
- Rating: `.star-rating` class (converted to number)
- Availability: `.availability` class
- Link: `<a href="...">` attribute

### 5. **Handle Pagination**
```python
next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
```

### 6. **Save Output**
```python
df.to_csv("books.csv", index=False)
df.to_json("books.json", orient="records", indent=4)
```

## 🔧 Code Breakdown

### Helper Function: `get_rating()`
Converts star rating classes to numeric values:
- `"star-rating One"` → `1`
- `"star-rating Two"` → `2`
- `"star-rating Three"` → `3`
- etc.

### Error Handling
Each field uses `try-except` blocks to gracefully handle missing data:
```python
try:
    title = book.find_element(By.TAG_NAME, "h3")...
except:
    title = "N/A"  # Sets default if not found
```

## 🎨 Customization

### Adjust Delay Between Pages
```python
time.sleep(2)  # Increase to be more respectful (5 or 10)
```

### Export to Excel
```python
df.to_excel("books.xlsx", index=False)  # Add openpyxl to requirements
```

### Filter by Price or Rating
```python
# Filter books under £20
cheap_books = df[df['Price'].str.replace('£', '').astype(float) < 20]
```

## 🛠️ Selenium Selector Reference

```python
By.CSS_SELECTOR      # ".classname", "#id", "tag.class"
By.TAG_NAME          # "h3", "a", "div"
By.CLASS_NAME        # "price_color"
By.ID                # "main-content"
By.XPATH             # "//button[@class='next']"
```

### Finding Elements
```python
find_element()       # Returns first match (or raises exception)
find_elements()      # Returns list of all matches
```

## 🚨 Common Issues & Solutions

### Error: "ChromeDriver not found"
```python
# Make sure ChromeDriver is in PATH or specify path:
driver = webdriver.Chrome("/path/to/chromedriver")
```

### Error: "No such element exception"
- Website structure changed
- Use browser DevTools (F12) to inspect current selectors
- Update CSS selectors in the code

### Script runs but no data
- Check internet connection
- Increase `time.sleep()` value
- Verify website still exists and has same structure

### Too slow?
- Decrease `time.sleep()` value (but be respectful)
- Consider adding timeout parameters to element searches

## ⚠️ Web Scraping Ethics

✅ **DO:**
- Check website's `robots.txt`
- Read Terms of Service
- Add delays between requests
- Use user-agent headers responsibly
- Respect rate limits

❌ **DON'T:**
- Overload servers with rapid requests
- Scrape copyrighted content without permission
- Bypass authentication or paywalls
- Ignore robots.txt or ToS

### About This Website
[books.toscrape.com](https://books.toscrape.com) is an **official practice site** created specifically for learning web scraping. ✅ **Safe to scrape!**

## 📚 Learn More

- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Pandas DataFrame Guide](https://pandas.pydata.org/docs/)
- [CSS Selectors Tutorial](https://www.w3schools.com/cssref/selectors.asp)
- [XPath Guide](https://www.w3schools.com/xml/xpath_syntax.asp)

## 📝 Project Structure

```
books-scraper/
├── scrap.py              # Main scraper script
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── .gitignore           # Git ignore rules
├── books.csv            # Output (generated)
└── books.json           # Output (generated)
```

## 🎯 Next Steps

1. **Run the scraper** - See it work in real-time
2. **Review the output** - Check books.csv and books.json
3. **Modify selectors** - Inspect HTML to find new targets
4. **Add features** - Filter, aggregate, or visualize data
5. **Deploy** - Schedule with cron jobs or AWS Lambda

## 📄 License

This project is for **educational purposes only**. Respect the terms of service of any website you scrape.

---

**Happy Scraping!** 🎉

Made with ❤️ for learning Selenium & web scraping
