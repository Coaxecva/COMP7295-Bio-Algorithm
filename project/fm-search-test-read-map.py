#!/usr/bin/python
import os
from os.path import join, abspath, isfile, isdir, exists, basename
import time

import sys
import fmindex
import tarfile
from os import walk
from os import listdir
from os.path import isfile, join

def diff_time(start, end):
    return int((end - start) * 1000)

import os

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

def concat_rc(gem):
    tmp = ""
    for nu in gem:
        if nu =="A":
            tmp += "T"
        elif nu == "T":
            tmp += "A"
        elif nu == "C":
            tmp += "G"
        else:
            tmp += "C"
    return gem + "|" + tmp[::-1]

def main():
    
    tim = time.clock
    index = []
    # Run the above function and store its results in a variable.   
    full_file_paths = get_filepaths(sys.argv[1])
    #print(full_file_paths)
    
    t_start = tim()

    for f in full_file_paths: 
        print(f)  
        inp = open(f)
        
        # read input
        data = inp.read()
        s = data.split('\n', 1)[-1].replace("\n", "")
        
        #print(concat_rc(s))
        index.append(fmindex.index(concat_rc(s)))

    t_load = tim()
    print("Number of genomes: " + str(len(index)))
    print("Indexing: %sms" % diff_time(t_start, t_load))

    time.sleep(5)

    lines2 = [line.rstrip('\n') for line in open(sys.argv[2])]
    lines3 = [line.rstrip('\n') for line in open(sys.argv[3])]

    #print(lines2)

    idx2 = []
    idx3 = []
    read2 = []
    read3 = []
    for i in range(len(lines2)):
        if i%4 == 0:
            idx2.append(lines2[i])
            idx3.append(lines3[i])

    for i in range(len(lines3)):
        if i%4 == 1:
            read2.append(lines2[i])
            read3.append(lines3[i])

    #print(idx2)
    #print(read2)

    for r in range(len(read2)):
        print(read2[r])
        print(idx2[r])
        tmp1 = tim()
        for i in range(len(index)):
            if index[i].search(read2[r]):
                #print(index[i].search(r))
                print(full_file_paths[i])
                time.sleep(0.5)
                break
        tmp2 = tim()
        print("Search: %sms" % diff_time(tmp1, tmp2))

    for r in range(len(read3)):
        print(read3[r])
        print(idx3[r])
        tmp1 = tim()
        for i in range(len(index)):
            if index[i].search(read3[r]):
                #print(index[i].search(r))
                print(full_file_paths[i])
                time.sleep(0.5)
                break
        tmp2 = tim()
        print("Search: %sms" % diff_time(tmp1, tmp2))

    # with open(sys.argv[2]) as f2, open(sys.argv[3]) as f3:
    #     content2 = f2.readline()
    #     content3 = f3.readline()
    #     print(content2)
    #     print(content3)

    # if not len(sys.argv) in [3]:
    #     print 'Usage: '
    #     print '  %s index search_string' % sys.argv[0]
    #     os.abort()
    # else:
    #     if not isfile(sys.argv[1]):
    #         print "Index file doesn't exist"
    #         os.abort()
        
    #     tim = time.clock
        
    #     t_start = tim()
        
    #     idx = fmindex.load(sys.argv[1])
    #     t_load = tim()
        
    #     c = idx.count(sys.argv[2])
    #     t_count = tim()
        
    #     m = idx.search(sys.argv[2])
    #     t_search = time.clock()
    #     print "load: %sms" % diff_time(t_start, t_load)
    #     print "count: %sms" % diff_time(t_load, t_count)
    #     print str(c)
    #     print "matches: %sms" % diff_time(t_count, t_search)
    #     print str(m)

if __name__ == '__main__':
    main()