import urllib
import bs4 as BeautifulSoup

from random import randint

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    # url = 'https://communities.apple.com/fr/message/' + str(randint(220010632, 220039330))
    url = 'https://communities.apple.com/de/message/200031820'
    response = urllib.urlopen(url).read()
    soup = fetch_curated_soup(response)

    

    response_list = get_responses(soup)

    # xml_string = ""

    # for x in xrange(1000000,2000000):
    #     url = 'https://communities.apple.com/de/message/' + x

    #     response = urllib.urlopen(url).read()
    #     soup = fetch_curated_soup(response)
    #     usernames = get_usernames(soup)

    #     if (valid_conversation(usernames)):
    #         write_to_xml(xml_string, soup)
    #     else:
    #         continue
    

def fetch_curated_soup(url_response):
    soup = BeautifulSoup.BeautifulSoup(url_response, "lxml")

    recommendation = soup.find('div', {"class": "recommended-answers"})
    persist = soup.find('div', {"class": "persist-question"})

    # Trim clutter from the soup 
    if recommendation is not None:
        recommendation.decompose()

    if persist is not None:
        persist.decompose()

    return soup 
    
def get_usernames(soup):
    username_data = soup.findAll("a", attrs={'class': 'j-avatar'})
    username_list = [ data.attrs['data-username'] for data in username_data]
    return username_list

def get_responses(soup):
    response_data = soup.findAll("div", attrs={"class": "jive-rendered-content"})
    response_list = []

    for data in response_data:
        response_list.append(data.findAll('p', 'span', 'a', 'ul', 'ol').text)

    return response_list

def valid_conversation(usernames):
    return True

def write_to_xml(file_string, soup): 
    return True

if __name__ == '__main__':
    main()
