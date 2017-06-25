#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup  # need to install library first.

# specify which page to scrape
url = 'https://github.com/showcases/machine-learning'

# adding headers to mask the fact that this is a program
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# making a request with the headers we created
req = urllib.request.Request(url, headers=headers)

# sending the request
resp = urllib.request.urlopen(req)

# reading the resulting html and saving it to 'html'
html = resp.read()

# pass html to beautiful soup for parsing
soup = BeautifulSoup(html, 'html.parser')

# find all tags
tagged_values = soup.find_all('h3', {'class': 'mb-1'})
print(tagged_values)

# extracting text/content and saving it to 'values'
values = [x.get_text() for x in tagged_values]

# print scrapped values
for value in values:
    print(value)

# print newline
print('\n')
