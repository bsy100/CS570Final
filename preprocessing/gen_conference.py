# ID, SHORTNAME, FULLNAME, Homepage

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
    f = open("../data/old_data/OldConference.csv", "r")
    fout = open("../data/Conference.csv", "w")
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
        
        
    f.close()
    fout.close()
    f_stop.close()
    
if __name__ == "__main__":
    main()