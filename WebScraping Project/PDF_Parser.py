import io
import os
import threading
import queue
from multiprocessing.pool import ThreadPool
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

q = queue.Queue()
p = ThreadPool()
listofpdf={}

def convert_pdf_to_txt(path):
    print(path+"\n")
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    laparams = LAParams()

    with io.StringIO() as retstr:
        with TextConverter(rsrcmgr, retstr, codec=codec,
                           laparams=laparams) as device:
            with open(path, 'rb') as fp:
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                password = ""
                maxpages = 0
                caching = True
                pagenos = set()

                for page in PDFPage.get_pages(fp,pagenos,maxpages=maxpages,password=password,caching=caching,check_extractable=True):
                    interpreter.process_page(page)

                content = retstr.getvalue()

                listofpdf[content.count(phrase)] = path
                



def mainpharse(path,phr):

    global phrase
    phrase = phr
    
    if ".pdf" in  os.listdir(path):

        path = path + "\\.pdf\\"
        listofpdf={}
        os.chdir(path)
        print("\n\nSearching for relevant PDF's for the Phrase : '"+phrase+"'")
        pdfs = os.listdir(path)

        p.map(convert_pdf_to_txt,[i for i in pdfs])
        p.close()

        keys = []
        for i in listofpdf:
            keys.append(i)
        keys.sort(reverse = True)
        print("\n\nThe Highly relevant PDF's to the Phrase" + phrase + " are : ")
        try:
            for i in range(0,5):
                print(str(i+1) + ") "+listofpdf[keys[i]])

        except IndexError:
            None
       # return True
       
        
    else:
        print("No PDF's Found !!")
      #  return False
    
            
