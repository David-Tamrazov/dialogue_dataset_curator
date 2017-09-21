import urllib
import bs4 as BeautifulSoup

from random import randint

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():

    xml_string = "<dialog>\n"

    for x in xrange(200031820,200032820):
       
        # if x == 200031830:
        #     break
        
        url = 'https://communities.apple.com/de/message/' + str(x)

        response = urllib.urlopen(url).read()
        soup = fetch_curated_soup(response)

        response_divs = soup.findAll("div", attrs={"class": "jive-rendered-content"})
        username_links = soup.findAll("a", attrs={'class': 'j-avatar'})

        response_list = [get_response_text(div) for div in response_divs]
        username_list = get_usernames(username_links)

        if valid_conversation(username_list):
            xml_string += write_to_xml(response_list, username_list)+"\n"
            # print(write_to_xml(response_list, username_list)+"\n")
    
    xml_string += "</dialog>"



    file = open("curated_dataset.xml", "w")
    file.write(xml_string)
    file.close()

def fetch_curated_soup(url):
    response = urllib.urlopen(url).read()
    soup = BeautifulSoup.BeautifulSoup(response, "lxml")

    recommendation = soup.find('div', {"class": "recommended-answers"})
    persist = soup.find('div', {"class": "persist-question"})

    # Trim clutter from the soup 
    if recommendation is not None:
        recommendation.decompose()

    if persist is not None:
        persist.decompose()

    return soup 
    
def get_usernames(username_data):
    username_list = [ data.attrs['data-username'] for data in username_data]
    return username_list

def get_response_text(response_div):
    response_elements = response_div.findAll(["p", "a", "span", "ul", "ol"])

    response = ""

    for element in response_elements:
        response += element.text

    return response

def valid_conversation(usernames):
    return len(set(usernames)) > 1 and len(usernames) > 1
        

def write_to_xml(response_list, username_list): 
    output = "<s>"
    for i in xrange(0, len(response_list)):
        output += "<utt uid="+'"'+username_list[i]+'"'+">"+response_list[i]+"</utt>"
    output += "</s>"    
    return output

if __name__ == '__main__':
    main()
