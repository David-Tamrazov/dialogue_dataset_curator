import urllib
import bs4 as BeautifulSoup

from random import randint

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://communities.apple.com/fr/message/' + str(randint(220010632, 220039330))

print(url)

response = urllib.urlopen(url).read()
# print response[:1000]
print "\n"
# print(type(response))
soup2 = BeautifulSoup.BeautifulSoup(response, "lxml")

# print(type(soup2))
searchterm = ["j-thread-post", "all-replies-container"]
# print searchterm[0]

for p in range(0, 2):
    section = str(soup2.find("div", {"class": searchterm[p]}))
    soup3 = BeautifulSoup.BeautifulSoup(section, "lxml")

    # print((soup3))
    # print("test")

    usernameSoup = soup3.find(text='data-userid')

    userSoup = soup3.findAll("div", {"class": "jive-rendered-content"})  # , limit=10

    # print usernameSoup

    length = len(userSoup)

    # print(length)

    for x in range(0, length):
        t = userSoup[x]

        lol = t.findAll("p")
        length2 = len(lol)

        for z in range(0, length2):
            y = lol[z]
            print(y.text)

        print "\n\n"

        # print usernames
