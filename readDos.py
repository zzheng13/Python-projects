import urllib.request

def getPageContent(link):
    
    if link[0] == "h":
        connection = urllib.request.urlopen(link)
        data = connection.read()
        data = data.decode('utf-8')
        return data 
        
    elif link[4] == ":":
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
        
        
        
        


        
            
    elif link[0] == "w":
        mystr = "http://"
        link = mystr + link
        connection = urllib.request.urlopen(link)
        data = connection.read()
        data = data.decode('utf-8')
        return data                             

    elif link[0] != "h" and link[0] !="w" and link != "f":
        f = open(link)
        data = f.readline()
        string = ""
        while data:
            
            string = string + data
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

            
        
                       












