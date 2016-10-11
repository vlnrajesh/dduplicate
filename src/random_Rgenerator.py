#!/usr/bin/env python
try:
    import random
    import os
    import csv
    import sys
except ImportError,err:
    print err


if __name__ == '__main__':
    file_name=raw_input("Enter destination file name : ")
    min_number=int(raw_input("Enter Minimum number of range : "))
    max_number=int(raw_input("Etner Maximum number of range : "))
    nrr= int(raw_input("No of records for row  : "))
    open(file_name, "a")
    stat_info=os.stat(file_name)
    data=[]
    if os.path.exists(file_name):
        stat_info = os.stat(file_name)
        while stat_info.st_size <=1048576:
            stat_info = os.stat(file_name)
            _list = [random.randint(min_number,max_number) for x in range(0,nrr)]
            _list = [ "%04d" %x for x in _list]
            data.extend(_list)
            if len(data) >= 100:
                with open(file_name,'a') as fp:
                    wp=csv.writer(fp,delimiter=',')
                    wp.writerow(data)
                data=[]
    print "Random R generated on %s" %file_name
    sys.exit(0)

