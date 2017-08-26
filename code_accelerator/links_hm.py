#url = raw_input("Enter a website to extract the URL's from: ")
# python 2
import urllib2
from bs4 import BeautifulSoup


def get_all_links(page, tag, attribute):
    image_page = page
    page = urllib2.urlopen(image_page)
    soup = BeautifulSoup(page, "html.parser")
    for link in soup.find_all(tag):
    	print(link.get(attribute))



books = URL + "/books"

print(get_all_links(URL, 'a', 'href'))
print(get_all_links(books,'img', 'src'))