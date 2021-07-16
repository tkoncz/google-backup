from bs4 import BeautifulSoup
import re

html = open('data/Albums - Google Photos2.html', 'r')
soup = BeautifulSoup(html, 'html.parser')

regex_num_items = re.compile(r'(?P<num_items>\d+)')
regex_shared = re.compile(r'(?P<shared>Shared)')

albums_html = soup.find_all(class_="fykiDc")
albums = []
for album in albums_html:
    album_title = album.find(class_="mfQCMe").text
    album_num_items = regex_num_items.search(
        album.find(class_="UV4Xae").text).group("num_items")
    album_is_shared = regex_shared.search(
        album.find(class_="UV4Xae").text) is not None

    albums.append({
        "album_title": album_title,
        "num_items": int(album_num_items),
        "is_shared": album_is_shared
    })

# print(albums)
print(albums[0])
