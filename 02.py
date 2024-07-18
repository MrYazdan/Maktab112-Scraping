# pip install requests
import requests

# pip install beautifulsoup4
import bs4

# zoomit_content = requests.get("https://www.zoomit.ir/").content
# soup = bs4.BeautifulSoup(zoomit_content, 'html.parser')

# Search document: ( find

# print(soup.find('title').text)
# print(soup.find('h1'))
# print(len(soup.find_all('h2')))

# print(soup.find('h2', class_="hmWIXE").text)
# print(soup.find(class_="hmWIXE").text)
# print(soup.find(id="__next").name)
# print(soup.find('a')['href'])

# CSS Selectors:

varzesh3_content = requests.get("https://www.varzesh3.com/").content
soup = bs4.BeautifulSoup(varzesh3_content, 'html.parser')

# print(soup.find(id="new").find(class_="videobox").find_all('a'))
# print(*[tag.text for tag in soup.find_all('h3')], sep="\n")

print(*[tag.text for tag in soup.select("#new .videobox a:last-child > h3")], sep="\n")
