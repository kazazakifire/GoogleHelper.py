"""
A program that takes a question from the command line and searches on Google. It will also open the first four links in new tabs.
"""

"""
Steps
    Accept input from command line
    Get input
    Create google search string
    Open browser with google search string
    Get search result
    Get top four links in search result.
    Open all links in new tabs.

//required modules
-webbrowser
-requests_html [https://pypi.org/project/requests-html/]
    to install : pip install requests-html (run on command line)
"""

# you can take input using the sys.argv variable. 

from requests_html import HTML, HTMLSession
import sys #for argv
import webbrowser

GOOGLE = 'https://www.google.com/search?q=' #constant for search query

while True:
    if len(sys.argv) <=1:
        print('Usage: python GoogleHelper.py your search query here')
        sys.exit()
    else:
        break

# get the search query and from a string with it.

userQuery = sys.argv[1:]
print(userQuery)

searchString = GOOGLE + "+".join(userQuery)

print(searchString)
webbrowser.open(searchString)

# we want to get the results of the page

session = HTMLSession() #first create a session object
r = session.get(searchString)                    #use the session object to make a request. this will return a response object.
print(r.html) #this is the html object element. to get the html of an element, use html.html, else use html.text to see just text contents.

htmlObject = r.html

linkSelector = '.g .rc .r a'
print(linkSelector)
titleSelector = 'div.r a h3'

links = htmlObject.find(linkSelector)
resultLinks = []
titles = []

print('While loop starts here')
for link in links:

    href = link.attrs['href']


    if href.startswith('https://webcache.googleusercontent.com/') or href == '#' or href.startswith('/search'):
        continue
    else:
        print(f'Seen a valid link:\t{href}')
    
    if href not in resultLinks:
        resultLinks.append(href)

    if(len(resultLinks)==10):
        break


for link in resultLinks:
    webbrowser.open_new_tab(link)
