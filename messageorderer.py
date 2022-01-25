import sys
generaldict = dict()
linelist = []
output = open("{}".format(sys.argv[2]), "w")
with open("{}".format(sys.argv[1]), "r+") as firstfile:
    linenumbers = []
    for line in firstfile:
        linelist.append(line.strip().split("\t"))
    for lineno in linelist:
        if lineno[0] not in linenumbers:
            linenumbers.append(lineno[0])
    sortinglist = []
    for classed in range(len(sorted(linenumbers))):
        writelist = []
        for check in linelist:
            if check[0] == sorted(linenumbers)[classed]:
                writelist.append(check)
        writelist.sort()
        output.write("Message {}\n".format(classed+1))
        for writings in range(len(writelist)):
            for sublist in writelist[writings]:
                sublist = sublist + "   "
                output.write(sublist)
            output.write("\n")
        output.write("\n")

        
        
   
