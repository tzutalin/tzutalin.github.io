from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html"), 'html.parser')

div = soup.find(id="opensource")
print div.findNext('ul')
