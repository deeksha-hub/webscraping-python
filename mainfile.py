import requests                                    #importing requests module
import bs4                                         #importing beautiful soup
import json                                        #importing JSON
import lxml
res = requests.get('https://time.com')             #sends a GET request to the specified URL

soup = bs4.BeautifulSoup(res.text,'lxml')          #retrieve the HTML content as text

hi = soup.select('.media-heading')                 #extracting data from class name "media-heading"
#print(hi)
links = []
list2 = []
list4 = []
data = soup.findAll('div', attrs={'class':'media-heading'})  #extracting links from the class "media-heading" synt=tag,tag  articlebody
for div in data:
    links = div.findAll('a')
    contents = div.findAll('a')
    for a in links:
        s=""
        s+= "https://time.com/" + a['href']                  #joining "https://time.com/" string and the link extracted
        list2.append(s)
    for a in contents:
        s1=""
        s1+=a.contents[0]
        s1=s1.strip('\n\t')                                  # to strip out the line breaks and tab
        s1=s1.lstrip()                                       # to remove spaces from from and end
        s1=s1.rstrip()
        list4.append(s1)
link = []
#print("links")
for i in range(4,10):
    link.append(list2[i])

#for i in range(len(link)):
    #print(link[i])
#for i in contents:
   # list4.append(contents)
#for i in range(len(list4)):
  #  print(list4[i])

#print("contents")
content = []

for i in range(3,9):
    content.append(list4[i])

print("JSON OBJECT")

mydict={'news':[{'titles':t,"link":s}for t ,s in zip(content, link)]}    # dictionary to represent the data
print(json.dumps(mydict))                                                # convert python to json object
