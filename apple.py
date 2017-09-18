import urllib
import bs4 as BeautifulSoup

from random import randint

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    # url = 'https://communities.apple.com/fr/message/' + str(randint(220010632, 220039330))
    url = 'https://communities.apple.com/de/message/200031820#200031820'

    print(url)

    response = urllib.urlopen(url).read()
    # print response[:1000]
    print "\n"

    # print(type(response))
    soup = BeautifulSoup.BeautifulSoup(response, "lxml")

    get_post_author(soup)
    get_usernames_of_replies(soup)

    # # print(type(soup2))
    # searchterm = ["j-thread-post", "all-replies-container"]

    # print searchterm[0]

    # for p in range(0, 2):
    #     section = str(soup.find("div", {"class": searchterm[p]}))
    #     soup2 = BeautifulSoup.BeautifulSoup(section, "lxml")

    #     # print((soup3))
    #     # print("test")

    #     usernameSoup = soup.find(text='data-userid')

    #     userSoup = soup.findAll("div", {"class": "jive-rendered-content"})  # , limit=10

    #     # print usernameSoup

    #     length = len(userSoup)

    #     # print(length)

    #     for x in range(0, length):
    #         t = userSoup[x]

    #         lol = t.findAll("p")
    #         length2 = len(lol)

    #         for z in range(0, length2):
    #             y = lol[z]
    #             print(y.text)

    #         print "\n\n"

    #         # print usernames

def get_post_author(soup):
    div_data = soup.find("div", "j-post-author")
    link_data = div_data.find("a").attrs
    author = link_data['data-username']
    return author

def get_usernames_of_replies(soup):
    replies = soup.findAll("a", attrs={'class': 'j-avatar'})
    username_list = [ reply.attrs['data-username'] for reply in replies]
    return username_list

if __name__ == '__main__':
    main()
