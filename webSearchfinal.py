import urllib.request
import sys
import math
# ----------------------------------countdoc --------------------------------
def countdoc(L):
    num = len(L)
    return num
    

#----------------------------------papa1(can be used for "P") -------------------------------------

def woCao(filename):

    f = open(filename,"r")
    nextline=f.readline()
    
    p=[]
    j = []
    while nextline !="":
        nextline = nextline.strip(",.;:\"\'?!+=")
        nextline = nextline.strip("\n")
        
        
        p.append(nextline)
        nextline=f.readline()

    for i in range(len(p) - 1):
        if p[i] == '':
            del(p[i])
    del(p[-1])
            
    return p

def woCao1(filename):

    f = open(filename)
    nextline=f.readline()
    mystr=""
    p=[]
    while nextline !="":
        nextline = nextline.strip("\n")
        p.append(nextline)
        nextline=f.readline()

        
    return p
#------------------------------------- get string of files-----------------
def getPageContent(link):
    
    if link[0] == "h" and link[1] == "t" and link[2] == "t" and link[3] == "p":
        connection = urllib.request.urlopen(link)
        data = connection.read()
        data = data.decode('utf-8')
        return data 
        
    elif link[3] == "e" and link[4] == ":":
        x = link.replace(":"," ")
        List = x.split()
        link = List[1]
        f = open(link)
        data = f.readline()
        string = ""
        while data:
            
            string = string + data
            data = f.readline()

        return string 
        
        
    elif link[0] == "w" and link[1] == "w" and link[2] == "w":
        mystr = "http://"
        link = mystr + link
        connection = urllib.request.urlopen(link)
        data = connection.read()
        data = data.decode('utf-8')
        return data                             

    else:
        f = open(link)
        data = f.readline()
        string = ""
        while data:
            
            string = string + data
            string = string.strip("\n")
            data = f.readline()

        return string 
     
        

def stripTags(testHTML):
    result = ""
    tag = False
    for i in range(len(testHTML)):
        if testHTML[i] == "<":
            tag = True
           
        if not tag:
            result = result + testHTML[i]
            
        if testHTML[i] == ">":
            tag = False
            
    return result

#--------------------------------------getlink (can be used for "s")--------------
def getword(L):
    m = {}
    p = []
    i = 0
    j = []
    while i < countdoc(woCao(sys.argv[1])):
        
        m[L[i]] = i
        i = i + 1
    return m

def getDirt(diction):
    p= []
    j = []
    i = 0
    u = 0
    while i < countdoc(woCao(sys.argv[1])):
        
        for key in diction:
            if diction[key] == i:
                string = stripTags(getPageContent(key))
                p.append(string)
        i = i + 1

    while u < countdoc(woCao(sys.argv[1])):
        
        
        s=p[u]
        s=s.strip(",.;:\"\'?!+=")
        k=s.split()
        j.append(k)
        u = u + 1 
    return j                        # return a dictionary of files 
# ------------------------------------------------------------------------------
def get(L):
    m = {}
    p = []
    i = 0
    j = []
    while i < countdoc(woCao(sys.argv[1])):

        
        m[L[i]] = i
        i = i + 1
    return m

def dic(L):
    ziDian={}
    i=0
    s=set()
    while i < countdoc(woCao(sys.argv[1])):
        
        for word in L[i]:
        
            
            w=word.strip(",.;:\"\'?!+=")
            w = w.lower()
            
            if (w in ziDian):
                k=i
                
                
                s = set([k])
                ziDian[w]=ziDian[w].union(s)
                
            else:
                k=i
               
                ziDian[w]=set([k])
        i = i + 1 
               
    
    return ziDian


#---------------------------------------------------------------------
def countdocs(filename):
    f=open(filename,"r")
    num=0
    for line in f:
        num=num+1
    return num    


def main():
    print(str(countdocs(sys.argv[1]))+"documents parsed")
    html=0
    outputFile=0
    
    name=input("What do you want to do?\n"
                "(S)earch the documents\n"
                "(P)rint out a document\n"
                "(Q)uit\n"
                "Enter s,p or q:\n")
    while name!="q":
        if name=="s":
            term=input("Enter search terms:")
            m=dam()
            n = dictionary()
            term=term.split()
            r = []
            w=[]
            
            if len(term)==1:
                t = ""
                if term[0] in n:
                    for key in m:
                        for x in n[term[0]]:
                            if x == m[key]:
                                r.append(key)
                                
    
            elif len(term) >= 2:
       
                for word in term:
                    t = set()
                    if word in n:
                        t = t.union(set(n[word]))
                
                for word in term:
                    if word in n:
                        t = t.intersection(set(n[word]))
            
                for key in m:
                    for e in t:
                        if e == m[key]:
                            r.append(key)

        # r list all
            if len(term)==1:
                t = ""
                if term[0] in n:
                    for key in m:
                        for x in n[term[0]]:
                            if x == m[key]:
                                w.append(key)
                                
    
            elif len(term) >= 2:
                t = set()
                for word in term:
                    if word in n:
                        for key in m:
                            for e in n[word]:
                                if e == m[key]:
                                    w.append(key)
        # return  w some
                
            html ="<html><head><title>'The out put'</title><link rel='stylesheet' type='text/css' href='style.css'/></head><body> <div id='container'><div id='header'><h1> Search for : " +san(term)+" </h1></div>" +"<div id='content'><h1> Results </h1></div><div id='all'><h1> Documents Matching all search terms</h1><div id='alllist'><h4>"+ createHTMLTableLine(r)+"</h4></div><div id= 'some'><h1>Documents Matching some(but not all) search terms</h1>"+createHTMLTableLine(w)+ createHTMLFooter()
            outputFile = open("output.html", "w")
            outputFile.write(html)
            outputFile.close()
            print("Output written to output.html")

            name=input("What do you want to do?\n"
                    "(S)earch the documents\n"
                    "(P)rint out a document\n"
                    "(Q)uit\n"
                    "Enter s,p or q:\n")
        elif name=="p":
            num=input("Enter document number:")
            num=int(num)
            m=dam()
            if num>countdoc(woCao(sys.argv[1])):
                
                print("Too big")
            else:
                for key in m:
                    if num == m[key]:
                        k = key 
                print (k)
                       
            name=input("What do you want to do?\n"
                   "(S)earch the documents\n"
                   "(P)rint out a document\n"
                   "(Q)uit\n"
                   "Enter s,p or q:\n")
    return 

def dam():
    return get(woCao(sys.argv[1]))
 
def dictionary():
    return dic(getDirt(getword(woCao(sys.argv[1]))))

def san(wordd):
    st = ""
    s = wordd
    for e in s:
        st = st + str(e) + " " 
    return st





#def createHTMLHeader():
    #return "<html><head><title>'The out put'</title><link rel='stylesheet' type='text/css' href='style.css'/></head><body> <div id='container'><div id='header'><h1> Search for : " +san(term)+" </h1></div>"

#def creatHTMLpara():
    #return "<div id='content'><h1> Results </h1></div><div id='all'><h1> Documents Matching all search terms</h1><div id='alllist'><h4>"+ createHTMLTableLine(r)+"</h4></div><div id= 'some'><h1>Documents Matching some(but not all) search terms</h1>"


def createHTMLTableLine(rowList):
    result =[]
    result=result+["<div id='somelist'>"]
    result=result+["<ul>"]
    for i in range (len(rowList)):
        rowList[i]=str(rowList[i])
    for word in rowList:
        k=["<li>", word ,"</li>"]
        sep=''
        sep=sep.join(k)
        result=result+[sep]
    result=result+["</ul>"]
    result=result+["</div></div></div>"]
    sep=""
    result=sep.join(result)
    return result

def createHTMLFooter():
    return "</body> </html>"



if __name__=="__main__":
    main()
  

    

                          

            
