#alphabet
alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#take input
string=input("string: ").lower()

#asign list of string to charlist
charlist=list(string)

#asign lenght of charlist to indexrange
indexrange=int(len(charlist))

#create out variable
out=""

#main loop
for rot in range(1,26):
    #internal loop
    for i in range (0, indexrange):
    
        #main if
        if charlist[i] in alpha:
    
            #internal loop
            for n in range(0,26):

                #nested if
                if alpha[n] == charlist[i]:
                   
                    #nested if
                    if n+rot > 25:
                        n -= 26
                    out+=alpha[n+rot]
        #else
        else:
            out+=charlist[i]
        
    #print output
    print(out)
    out=""
               
                   
               
               
               
                   
