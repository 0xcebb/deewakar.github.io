#!/usr/bin/env python3
import bs4
import json

sitemap_file = open("sitemap.html").read()
sitemap_soup = bs4.BeautifulSoup(sitemap_file, 'html.parser')

links = sitemap_soup.find(id='content').find_all('a')

# all html documents to be indexed
docs = [link.attrs.get('href') for link in links]

# page indexes
indexes = []

for doc in docs:
    docfile = open(doc).read()
    doc_soup = bs4.BeautifulSoup(docfile, 'html.parser')
    toc = doc_soup.find(id='text-table-of-contents').find('ul').find_all('a')
    
    for link in toc:
        text = link.decode_contents()
        url = doc + link.get('href')
        title = doc_soup.title.string
        d = {'text': text, 'url': url, 'title': title}
        indexes.append(d)


output = json.dumps(indexes)
print(output)
