from googlesearch import search
import requests
from bs4 import BeautifulSoup
import PDF_Parser
import urllib.request

def Relatable(path,word):   
    query = word + "wikipedia"
    results = []

  
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        results.append(j)

    html = urllib.request.urlopen(results[0])
    soup = BeautifulSoup(html,'html.parser')

    get_similar = set()

    print("\n\nRelated words to your Phrase are : \n")

    for link in soup.findAll("a"):
        if 'href' in link.attrs and link and not link.text.startswith('Jump') and not link.text.startswith('edit') and not word in link.text and not link.text.startswith('[') and link.text.isalpha():
            print(link.text)
            get_similar.add(link.text)
            if len(get_similar) > 5:
                break
    for i in get_similar:
        PDF_Parser.mainpharse(path,i)
        
        
        
    



