# PaperID, AuthorID, Name, Affiliation

def ascii(line):
    s = list(line)
    for i in range(len(s)):
        char = s[i]
        if ord(char) < 32 or ord(char) > 126:
            s[i] = ''
    return ''.join(s)

def remove_stopwords(line, stoplist):
    for s in stoplist:
        if (" " + s) in line:
            line = line.replace(" " + s, " ")
    return line

def Lower(line):
    return line.lower()

def make_stoplist(f):
    result = []
    for l in f:
        result.append(l[:-1])
    return result

def main():
    f = open("../data/old_data/PaperAuthor.csv", "r")
    fout = open("../data/PaperAuthor.csv", "w")
    f_stop = open("stopwords.txt", "r")
    
    # make a stopword list 
    stoplist = make_stoplist(f_stop)
    
    fout.write(f.readline())
    
    for line in f:
        l = Lower(line)
        l = ascii(l)
        l = remove_stopwords(l, stoplist)
        #fout.write(l)
        fout.write(l+ '\n')        
        
        '''
        l = Lower(line)
        items = (l.rstrip()).split(",")
        
        if len(items) < 4 :
            fout.write(l + '\n')
            continue
        
        # non-ascii remove processing  for Name and Affiliation
        items[2] = ascii(items[2])
        affiliation = ascii(''.join(items[3:]))
        
        # stopword remove processing for Name and Affiliation
        items[2] = remove_stopwords(items[2], stoplist)
        affiliation = remove_stopwords(affiliation, stoplist)

        fout.write(','.join(items[:3]) +',' + affiliation + '\n')
        '''
        
    f.close()
    fout.close()
    f_stop.close()
    
if __name__ == "__main__":
    main()