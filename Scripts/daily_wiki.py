# Fetches the daily wikipedia featured article
import requests
from scrapy.selector import Selector
import unicodedata
import re
from datetime import datetime

# Get today's date to scrape Wikipedia's "Today's Featured Article"
today = datetime.now()
date = today.strftime("%d-%m-%Y")

# Construct the path to TFA URL
month = today.strftime("%B")
day = today.day
year = today.strftime("%Y")
path = f"https://en.wikipedia.org/wiki/Wikipedia:Today%27s_featured_article/{month}_{day},_{year}"

# Get the associated TFA & clean it up
r = requests.get(path)
body = Selector(text=r.text).xpath('//*[@class="mw-parser-output"]/p//text()').getall()
body = [unicodedata.normalize("NFKD", part) for part in body]
body = "".join(body).strip()
body = re.sub(" \(Full article...\)$", "", body)

# Append the TFA to a text
with open(f"Today's_featured_article.txt", "a") as f:
    f.write(f"Today's featured article on {date}:\n")
    f.write(body + "\n")

