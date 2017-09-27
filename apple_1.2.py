import urllib
import bs4 as BeautifulSoup

# testing github

import os

from random import randint

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

xmlfile = '<?xml version="1.0" encoding="utf-8"?>\n'
xmlfile += "<dialog>"

loop = 0

while loop < 2:
    print(loop)
    # xmlfile += "<s>"
    xmltemp = ""
    xmltemp += "\n\t<s>"

    url = 'https://communities.apple.com/de/message/' + str(randint(02000, 12000))

    print(url)

    response = urllib.urlopen(url).read()
    # print response[:1000]
    # print "\n"
    # print(type(response))
    soup = BeautifulSoup.BeautifulSoup(response, "lxml")
    recommendation = soup.find('div', {"class": "recommended-answers"})
    persist = soup.find('div', {"class": "persist-question"})

    if recommendation is None:
        pass
    else:
        recommendation.decompose()

    if persist is None:
        pass
    else:
        persist.decompose()

    maingroup = soup.findAll("div", {"class": "jive-rendered-content"})
    # print(maingroup)
    username = soup.findAll("a", {"class": "j-avatar"})

    length = len(maingroup)
    length2 = len(username)

    # print length, length2
    tag = [0] * length
    uid = [0] * length

    for x in range(0, length):

        tag[x] = username[x].get('data-username')
        # print tag[x]

        if tag[x] in tag[:x]:
            uid[x] = uid[tag.index(tag[x])]
        else:
            uid[x] = max(uid) + 1

        # xmlfile += '<utt uid="' + str(uid[x]) + '">'
        xmltemp += '<utt uid="' + str(uid[x]) + '">'

        # print uid[x]
        t = maingroup[x]
        lol = t.findAll(["p", "span", "a", "li", "ol", "ul"])
        lengthly = len(lol)

        for z in range(0, lengthly):
            y = lol[z]
            # print(y.text)
            # xmlfile += str(y.text)
            xmltemp += str(y.text)
            # ET.SubElement(s, "utt", uid=str(uid[x])).text = str(y.text)

        # print "\n"

        # xmlfile += "</utt>"
        xmltemp += "</utt>"

    # xmlfile += '</s>\n'
    xmltemp += '</s>'
    # print("\n\n")

    print uid.count(1)
    if uid.count(1) < 2:
        print("nothanks")
    else:
        xmlfile += xmltemp
        loop += 1

    print "\n"

xmlfile += "\n</dialog>"
# print xmlfile
# xmlfile = xmlfile.decode('utf-8')


file = open(os.path.expanduser("~/Desktop/applepy_test.xml"), "w")
file.write(xmlfile)
file.close()
