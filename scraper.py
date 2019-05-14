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

print br.response().read()

