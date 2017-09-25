import urllib
import bs4 as BeautifulSoup

from random import randint

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():

    xml_string = "<dialog>" + "\n"

    start_index = 200031820
    iterations = 20
    for x in xrange(0,iterations):
        print "Progress: "+str(100*x/iterations)+"%"
        
        url = 'https://communities.apple.com/de/message/' + str((x+start_index))
        response = urllib.urlopen(url).read()

        soup = fetch_curated_soup(response)

        response_divs = soup.findAll("div", attrs={"class": "jive-rendered-content"})
        username_links = soup.findAll("a", attrs={'class': 'j-avatar'})

        response_list = get_responses(response_divs)
        username_list = get_usernames(username_links)

        if valid_conversation(username_list):
            xml_string += convert_to_xml(response_list, username_list)
            # print(write_to_xml(response_list, username_list)+"\n")
    
    xml_string += "</dialog>"

    write_to_file(xml_string)


def fetch_curated_soup(response):
    soup = BeautifulSoup.BeautifulSoup(response, "lxml")

    recommendation = soup.find('div', {"class": "recommended-answers"})
    persist = soup.find('div', {"class": "persist-question"})

    # Trim clutter from the soup 
    if recommendation is not None:
        recommendation.decompose()

    if persist is not None:
        persist.decompose()

    return soup 
    
def get_usernames(username_links):
    username_list = [ data.attrs['data-username'] for data in username_links]
    return username_list

def get_responses(response_divs):
    
    # define get_response_text within get_responses scope to keep it Private 
    def get_response_text(response_div):
        response_elements = response_div.findAll(["p", "a", "span", "ul", "ol"])

        response = ""

        for element in response_elements:
            response += element.text

        response = response.replace("&", "_and_").replace("@", "_at_").replace("<", "_open_angle_").replace(">", "_close_angle_")
        return response
    

    response_list = [get_response_text(div) for div in response_divs]
    return response_list

def valid_conversation(usernames):
    return len(set(usernames)) > 1 and len(usernames) > 1
        

def convert_to_xml(response_list, username_list): 
    output = "<s>"
    for i in xrange(0, len(response_list)):
        output += "<utt uid="+'"'+username_list[i]+'"'+">"+response_list[i]+"</utt>"
    output += "</s>" + "\n"  
    return output 

def write_to_file(xml_string):
    file = open("curated_dataset.xml", "w")
    file.write(xml_string)
    file.close()

if __name__ == '__main__':
    main()
