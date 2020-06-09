import requests
from bs4 import BeautifulSoup
from os.path import split
import os
from urllib.parse import urlparse
import shutil
import PDF_Parser
import RelatedPhrase



try:
   dirf = os.getcwd()
   get_extentions = set()
   l = False


   def Download_file(url,fname):
        print("Downloading the Files Requested")
        r = requests.get(url, stream = True)
        with open(fname,"wb") as f: 
          for chunk in r.iter_content(chunk_size= 1024*1024):
           if chunk: 
             f.write(chunk)
          get_extentions.add(os.path.splitext(fname)[-1])


          

   print("Enter a valid URL (ex: google.com ): ",end = "")
   rawurl = input()
   print("\nEnter a Phrase ")
   phrase = input() 
   if(rawurl.startswith('http')):
        url = rawurl
        
   else:
       url = "https://www."+rawurl
 

   if(not(split(urlparse(url).path)[-1])):
   

    rcontent = requests.get(url,allow_redirects=True,timeout = 10)
    

    print(rcontent)

    htmlcontent = rcontent.content    #2

    print("Sucess\n\n\n")

    soup = BeautifulSoup(htmlcontent,'html.parser')  	

    links = soup.find_all('a')  #4

    print("Searching for files......\n\n\n\n")
    
    get_links = set()
    

    print("Files Found are :\n")

    for i in links:
       if i.get('href')!= None:
         link = url+ i.get('href')
         get_links.add(link)

    for i in get_links :
      
       fln = split(urlparse(i).path)[-1]
       ext = os.path.splitext(fln)[-1]
   
       if(ext!=''):
           myfile = requests.get(i)
           if (ext) == '.com':
               print(fln)
               open("Links.txt",'a').write(fln+"\n")
               l = True
               
           else:
               print(fln)
               with requests.get(i, stream=True) as r:
                with open(fln, 'wb') as f:
                 shutil.copyfileobj(r.raw, f)
               get_extentions.add(ext)

   else:
            
            fname = (split(urlparse(url).path)[-1])
            Download_file(url,fname)

   

   if (len(get_extentions) == 0):
        print("\n\nNo Downloadable Files found")
        input()
        exit()


   os.mkdir(dirf +"\\-")

   print("\nCreating Folders and Organising Files")


   for i in get_extentions:
       os.mkdir(dirf +"\\-\\"+i)
       
                                            
   for i in os.listdir(dirf):
       folder = os.path.splitext(i)[-1]
       if (folder in get_extentions):
          shutil.move(i,dirf + "\\-\\" + folder)
   if l:
        shutil.move("Links.txt","-\\Links.txt")

    

   print("What would you like to Name the Folder With Data ? ")
   name=input()
   os.rename("-",name)


   print("\n\n\nChecking for Pdf Files with your Phrase")

   dirf = dirf+"\\"+name
     
   ispdffilethere = PDF_Parser.mainpharse(dirf,phrase)
   
   if ispdffilethere:
      print("\n\nSearching for Relatable Phrases")
      RelatedPhrase.Relatable(dirf,phrase)

   print("------Process Complete-------")
   
 

except requests.ConnectionError as exception:
   print("URL Does not exists , Please recheck URL")
except FileExistsError:
   print("Please Restart the program , deleting the '-' folder from directory")
   shutil.rmtree("-")
   for i in os.listdir():
      if not i.endswith('.py'):
         shutil.rmtree(i)
         
except Exception as e:
   print(e)
   for i in os.listdir():
      if not i.endswith('.py'):
         shutil.rmtree(i)
       
   
