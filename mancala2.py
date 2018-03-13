import sys
import zzheng13 
def main():
    if (sys.argv[1]=='human' and sys.argv[2]=='human')==True:
        k=creatBoard()
        b=k
        w=1
        while isGameOver(b, w)!=True:
            printBoard(b)
            #print(w)
            l=str(w)
            #print(l)
            name=input("Enter a move for player"+l+":\n")
            name=int(name)
            if legalMove(b,name,w)==True:
                #print(snatch(b,name,w))
                r=snatch(b,name,w)
                if (r=='0'or r=='7')==True:
                    w=w
                    #print('here')
                else:
                    if w==1:
                        w=2
                    elif w==2:
                        w=1
            elif legalMove(b,name,w)==False:
                print("Sorry, the move",name,"is invalid for player"+l)
        printBoard(b)
        w=str(w)
        print("Enter a move for player" +w+":\n")
        b[0]=b[0]+b[8]+b[9]+b[10]+b[11]+b[12]+b[13]
        b[8]=0
        b[9]=0
        b[10]=0
        b[11]=0
        b[12]=0
        b[13]=0
        b[7]=b[7]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]
        b[1]=0
        b[2]=0
        b[3]=0
        b[4]=0
        b[5]=0
        b[6]=0
        printBoard(b)
        if b[0]>b[7]:
            print("Player 2 wins,",b[0],"to",b[7])
        if b[0]<b[7]:
            print("Player 1 wins,",b[7],"to",b[0])
        if b[0]==b[7]:
            print("The match is a draw",b[0],"to",b[7])
    if (sys.argv[1]=='computer' and sys.argv[2]=='computer')==True:
        k=creatBoard()
        b=k
        w=1
        while isGameOver(b, w)!=True:
            printBoard(b)
            l=str(w)
            print("Enter a move for player"+l+":\n")
            name=zzheng13.computermove(b,w)
            if legalMove(b,name,w)==True:
                r=snatch(b,name,w)
                if (r=='0' or r=='7')==True:
                    #snatch(b,name,w)
                    w=w
                else:
                    #snatch(b,name,w)
                    if w==1:
                        w=2
                    elif w==2:
                        w=1
            elif legalMove(b,name,w)==False:
                print("Sorry, the move",name,"is invalid for player"+l)
        printBoard(b)
        w=str(w)
        print("Enter a move for player" +w+":\n")
        b[0]=b[0]+b[8]+b[9]+b[10]+b[11]+b[12]+b[13]
        b[8]=0
        b[9]=0
        b[10]=0
        b[11]=0
        b[12]=0
        b[13]=0
        b[7]=b[7]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]
        b[1]=0
        b[2]=0
        b[3]=0
        b[4]=0
        b[5]=0
        b[6]=0
        printBoard(b)
        if b[0]>b[7]:
            print("Player 2 wins,",b[0],"to",b[7])
        if b[0]<b[7]:
            print("Player 1 wins,",b[7],"to",b[0])
        if b[0]==b[7]:
            print("The match is a draw",b[0],"to",b[7])

    if (sys.argv[1]=='human' and sys.argv[2]=='computer')==True:
        k=creatBoard()
        b=k
        w=1
        r=0
        while isGameOver(b, w)!=True:
            if w==1:
                printBoard(b)
                l=str(w)
                name=input("Enter a move for player"+l+":\n")
                name=int(name)
                if legalMove(b,name,w)==True:
                    r==snatch(b,name,w)
                    if (r=='0' or r=='7')==True:
                        #snatch(b,name,w)
                        w=w
                    else:
                        #snatch(b,name,w)
                        if w==1:
                            w=2
                        elif w==2:
                            w=1
                elif legalMove(b,name,w)==False:
                    print("Sorry, the move",name,"is invalid for player"+l)
            if w==2:
                printBoard(b)
                l=str(w)
                print("Enter a move for player"+l+":\n")
                name=zzheng13.computermove(b,w)
                if legalMove(b,name,w)==True:
                    r=snatch(b,name,w)
                    if (r=='0' or r=='7')==True:
                        #snatch(b,name,w)
                        w=w
                    else:
                        #snatch(b,name,w)
                        if w==1:
                            w=2
                        elif w==2:
                            w=1
                elif legalMove(b,name,w)==False:
                    print("Sorry, the move",name,"is invalid for player"+l)
        printBoard(b)
        w=str(w)
        print("Enter a move for player" +w+":\n")
        b[0]=b[0]+b[8]+b[9]+b[10]+b[11]+b[12]+b[13]
        b[8]=0
        b[9]=0
        b[10]=0
        b[11]=0
        b[12]=0
        b[13]=0
        b[7]=b[7]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]
        b[1]=0
        b[2]=0
        b[3]=0
        b[4]=0
        b[5]=0
        b[6]=0
        printBoard(b)
        if b[0]>b[7]:
            print("Player 2 wins,",b[0],"to",b[7])
        if b[0]<b[7]:
            print("Player 1 wins,",b[7],"to",b[0])
        if b[0]==b[7]:
            print("The match is a draw",b[0],"to",b[7])
    if (sys.argv[1]=='computer' and sys.argv[2]=='human')==True:
        k=creatBoard()
        b=k
        w=1
        r=0
        while isGameOver(b, w)!=True:
            if w==1:
                printBoard(b)
                l=str(w)
                print("Enter a move for player"+l+":\n")
                name=zzheng13.computermove(b,w)
                if legalMove(b,name,w)==True:
                    r==snatch(b,name,w)
                    if (r=='0' or r=='7')==True:
                        #snatch(b,name,w)
                        w=w
                    else:
                        #snatch(b,name,w)
                        if w==1:
                            w=2
                        elif w==2:
                            w=1
                elif legalMove(b,name,w)==False:
                    print("Sorry, the move",name,"is invalid for player"+l)
                
            if w==2:
                printBoard(b)
                l=str(w)
                name=input("Enter a move for player"+l+":\n")
                name=int(name)
                if legalMove(b,name,w)==True:
                    r==snatch(b,name,w)
                    if (r=='0' or '7')==True:
                        #snatch(b,name,w)
                        w=w
                    else:
                        #snatch(b,name,w)
                        if w==1:
                            w=2
                        elif w==2:
                            w=1
                elif legalMove(b,name,w)==False:
                    print("Sorry, the move",name,"is invalid for player"+l)
        printBoard(b)
        w=str(w)
        print("Enter a move for player" +w+":\n")
        b[0]=b[0]+b[8]+b[9]+b[10]+b[11]+b[12]+b[13]
        b[8]=0
        b[9]=0
        b[10]=0
        b[11]=0
        b[12]=0
        b[13]=0
        b[7]=b[7]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]
        b[1]=0
        b[2]=0
        b[3]=0
        b[4]=0
        b[5]=0
        b[6]=0
        printBoard(b)
        if b[0]>b[7]:
            print("Player 2 wins,",b[0],"to",b[7])
        if b[0]<b[7]:
            print("Player 1 wins,",b[7],"to",b[0])
        if b[0]==b[7]:
            print("The match is a draw",b[0],"to",b[7])
        
def creatBoard():
    n=sys.argv[3]
    n=int(n)
    p= [0, n, n, n, n, n, n, 0, n, n, n, n, n, n]
    return p

def printBoard(list):
    a=" "
    print(a,13,12,11,10,9,8,7)
    print()
    print(a,list[13],list[12],list[11],list[10],list[9],list[8])
    print(list[0],a,a,a,a,a,a,list[7])
    print(a,list[1],list[2],list[3],list[4],list[5],list[6])
    print()
    print(0,1,2,3,4,5,6)

def legalMove(board, position, player):
    if player==1:
        if (position in [1,2,3,4,5,6]) and (board[position]>0)==True:
            return True
        else:
            return False
    if player==2:
        if (position in [8,9,10,11,12,13])and (board[position]>0)==True:
            return True
        else:
            return False



def isGameOver(board, player):
    if (player==1)and(board[1]==0)and(board[2]==0)and(board[3]==0)and(board[4]==0)and(board[5]==0)and(board[6]==0)==True:
        return True
    if (player==2)and(board[8]==0)and(board[9]==0)and(board[10]==0)and(board[11]==0)and(board[12]==0)and(board[13]==0)==True:
        return True
    else:
        return False
def snatch(board,position,player):
    m=[0,[2,3,4,5,6,7,8,9,10,11,12,13,1]*9,[3,4,5,6,7,8,9,10,11,12,13,1,2]*9,[4,5,6,7,8,9,10,11,12,13,1,2,3]*9, [5,6,7,8,9,10,11,12,13,1,2,3,4]*9,[6,7,8,9,10,11,12,13,1,2,3,4,5]*9,[7,8,9,10,11,12,13,1,2,3,4,5,6]*9,0,[9,10,11,12,13,0,1,2,3,4,5,6,8]*9,[10,11,12,13,0,1,2,3,4,5,6,8,9]*9,[11,12,13,0,1,2,3,4,5,6,8,9,10]*9,[12,13,0,1,2,3,4,5,6,8,9,10,11]*9,[13,0,1,2,3,4,5,6,8,9,10,11,12]*9,[0,1,2,3,4,5,6,8,9,10,11,12,13]*9]
    e=position
    i=board[position]
    if player ==1:
        if (m[position][i-1] in [1,2,3,4,5,6])==True:
            if (board[m[position][i-1]]==0)==True:
                #print('one')
                p=0
                o=board[position]
                while p<o:
                    board[m[position][p]]=board[m[position][p]]+1    
                    board[position]=board[position]-1
                    p=p+1
                board[7]=board[7]+board[m[position][i-1]]+board[14-m[position][i-1]]
                board[m[position][i-1]]=0
                board[14-m[position][i-1]]=0
        if (m[position][i-1]==7)==True:
            #print('two')
            p=0
            o=board[position]
            while p<o:
                board[m[position][p]]=board[m[position][p]]+1    
                board[position]=board[position]-1
                p=p+1
            print('player1')
            return '7'   
        else:
            #print('three')
            p=0
            o=board[position]
            while p<o:
                board[m[position][p]]=board[m[position][p]]+1    
                board[position]=board[position]-1
                p=p+1
    if player ==2:
        if (m[position][i-1] in [8,9,10,11,12,13])==True:
            if (board[m[position][i-1]]==0)==True:
                #print('four')
                p=0
                o=board[position]
                while p<o:
                    board[m[position][p]]=board[m[position][p]]+1    
                    board[position]=board[position]-1
                    p=p+1
                board[0]=board[0]+board[m[position][i-1]]+board[14-m[position][i-1]]
                board[m[position][i-1]]=0
                board[14-m[position][i-1]]=0
        if (m[position][i-1]==0)==True:
            #print('five')
            i=0
            o=board[position]
            while i<o:
                board[m[position][i]]=board[m[position][i]]+1    
                board[position]=board[position]-1
                i=i+1
            print('player2')
            return '0'
        else:
            #print('six')
            i=0
            o=board[position]
            while i<o:
                board[m[position][i]]=board[m[position][i]]+1    
                board[position]=board[position]-1
                i=i+1
    return
                
        
if __name__=="__main__":
    main()

    
