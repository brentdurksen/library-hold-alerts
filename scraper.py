import mechanize
import json
from bs4 import BeautifulSoup
import urllib2 
import cookielib

filename = "libcreds.json"

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://calgary.bibliocommons.com/holds")

if filename:
    with open(filename, 'r') as f:
        datastore = json.load(f)

br.select_form(nr=4)
br.form['name'] = datastore["username"]
br.form['user_pin'] = datastore["pin"] 
br.submit()

soup = BeautifulSoup(br.response().read(), "lxml")

for row in soup.find_all("div", "item-row item-header"):
    print(row.find("span", "title-content").get_text())
    print(row.find("span", "cp-subtitle").get_text())
    hold_position = row.find("span", "cp-hold-position")
    position_of_last_book = hold_position.strong.get_text()
    print("Position: " + position_of_last_book)
