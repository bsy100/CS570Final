'''
Created on 2015. 5. 27.

@author: jack
'''
import sys
import scipy.stats
import numpy
import math
import difflib

def run_main(cfile, sfile, rfile):
    
    cf = open(cfile, "r")
    sf = open(sfile, "r")
    rf = open(rfile, "a")
    
    tot_tau = 0
    idx = 0
    while 1:
        cline = cf.readline()
        if not cline: break
        clist1 = cline.split(',')[1]
        clist = clist1.split()
        print clist
        sline = sf.readline()
        slist1 = sline.split(',')[1]
        slist = slist1.split()
        print slist
        clen = len(clist)
        slen = len(slist)
        if clen > slen:
            clist = clist[0:slen]
        elif slen > clen:
            slist = slist[0:clen]
        #tau, p_value = scipy.stats.kendalltau(clist, slist)
        sm = difflib.SequenceMatcher(None,clist,slist)
        tau = sm.ratio()
        if not numpy.isnan(tau):
            tot_tau += math.fabs(tau)
            print tau
        idx = idx + 1
    print tot_tau
    result = cfile + "\t" + str(tot_tau) + "\n"
    rf.write(result)

if __name__=='__main__':
    if len(sys.argv) != 3:
        print >> sys.stderr, 'usage: <file to be compared> <result_file_name>'
    else:
        run_main(sys.argv[1], "testSolution.csv", sys.argv[2])