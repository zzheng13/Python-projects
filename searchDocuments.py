import sys

def san(string):
    liststring=string.split()
    for i in range(len(liststring)):
        liststring[i]=liststring[i].strip(",.;:""'+-=_?!")
        liststring[i]=liststring[i].lower()
    return liststring
                               

def para(filename):
    f = open(filename)
    nextline=f.readline()
    newline=nextline
    mystr=""
    p=[]
    while nextline !="":
        if nextline!=newline:
            mystr=mystr+str(nextline)
            nextline=f.readline()
        else:
            p.append(mystr)
            mystr=""
            nextline=f.readline()
    p.append(mystr)
    del(p[0])
    for i in range(len(p)):
        p[i]=san(p[i])
    return p


def para1(filename):
    f = open(filename)
    nextline=f.readline()
    newline=nextline
    mystr=""
    p=[]
    while nextline !="":
        if nextline!=newline:
            mystr=mystr+str(nextline)
            nextline=f.readline()
        else:
            p.append(mystr)
            mystr=""
            nextline=f.readline()
    p.append(mystr)
    del(p[0])
    return p

def getdic(L):
    wordd={}
    s=set()
    for i in range(countdoc(sys.argv[1])):
        for word in L[i]:
            if (word in wordd):
                k=i
                k=str(i)
                wordd[word].add(k)
            else:
                k=i
                k=str(k)
                wordd[word]=set(k)
    return wordd
    
def countdoc(filename):
    f=open(filename,"r")
    num=0
    for line in f:
        if line=="<NEW DOCUMENT>\n":
            num=num+1
    return num    

def main():
    print(str(countdoc(sys.argv[1]))+"documents parsed")
    name=input("What do you want to do?\n"
                   "(S)earch the documents\n"
                   "(P)rint out a document\n"
                   "(Q)uit\n"
                   "Enter s,p or q:\n")
    while name!="q":
        if name=="s":
            term=input("Enter search terms:")
            m=dictionary()
            term=san(term)
            t=set()
            if len(term)==1:
                if term[0] in m:
                    t=m[term[0]]
                else:
                    t="none"
            else:
                 t=[]
                 for word in term:
                     if word in m:
                         t.append(set(m[word]))
                     else:
                         t.append(set())
                 t= set.union(*t)
            tToPrint=""
            if t== set():
                tToPrint ="None"
            else:
                tPrint =t
                tPrint1=list(tPrint)
                tToPrint=" ".join(str(e) for e in tPrint1)
            print("Documents with search terms:"+tToPrint)
            name=input("What do you want to do?\n"
                   "(S)earch the documents\n"
                   "(P)rint out a document\n"
                   "(Q)uit\n"
                   "Enter s,p or q:\n")
        elif name=="p":
            num=input("Enter document number:")
            num=int(num)
            if num>=countdoc(sys.argv[1]):
                print("Too big")
            else:
                k=para1(sys.argv[1])[num]
                print (k)
            name=input("What do you want to do?\n"
                   "(S)earch the documents\n"
                   "(P)rint out a document\n"
                   "(Q)uit\n"
                   "Enter s,p or q:\n")
    return 


def dictionary():
    return getdic(para(sys.argv[1]))


if __name__=="__main__":
    main()

