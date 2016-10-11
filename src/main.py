#!/usr/bin/env python
try:
    from bplustree import *
    from hashtable import *
    import sys
    import os
    import csv
except ImportError, err:
    print err


class DDuplicate:

    def __init__(self,number_of_blocks=None,number_of_attribs=None):
        self._read_buffers=number_of_blocks-1
        self.number_of_attribs=number_of_attribs
        self.write_buffer = [None for x in range(self.number_of_attribs)]
        self.read_buffer =[self.write_buffer for y in range(self._read_buffers)]
        self.records=[]

    def open(self, filename):
        with open(filename) as fp:
            csv_reader = csv.reader(fp)
            for each_line in csv_reader:
                self.records.extend(each_line)
    def Getnext(self,type_of_index):
        if type_of_index == 'hash':
            ht=HashDict(self.number_of_attribs)
            while self.records:
                value=int(self.records.pop())
                ht.insert(value,value)
            self.close(ht,type_of_index)
        else:
            bt = BPTree(self.number_of_attribs)
            while self.records:
                bt.insert(self.records.pop())
            self.close(bt,type_of_index)

    def close(self,object,type_of_index):
        unique_records=object.keys()
        unique_records=[int(x) for x in unique_records]
        distinct_rows=[]
        for _each_slice in range(len(unique_records)):
            _slice = unique_records[:self.number_of_attribs]
            del unique_records[:self.number_of_attribs]
            if _slice: distinct_rows.insert(_each_slice,_slice)
        output_file='output_%s.txt' %type_of_index
        print "Writing results to %s" %output_file
        with open(output_file,'wb') as fp:
            wp = csv.writer(fp,delimiter=',')
            wp.writerows(distinct_rows)

def distinct(file_name=None, number_of_blocks=None, block_size=None, algorithm='btree'):
    try:
        number_of_blocks = int(number_of_blocks)
        block_size = int(block_size)
        if number_of_blocks < 2: raise ValueError("Invalid number of buffers")
        if not os.path.exists(file_name): raise ValueError("%s doesn't exist" %file_name )
        if not os.path.isfile(file_name): raise ValueError("%s is not a file" %file_name )
        if algorithm not in ['hash', 'btree']: raise ValueError('Invalid Algorithm - %s' %algorithm)
        dd = DDuplicate(number_of_blocks,block_size)
        dd.open(file_name)
        dd.Getnext(algorithm)

    except ValueError, err:
        print >> sys.stderr, err
        return None
   # except Exception, err:
   #     print err
if __name__ == '__main__':
    distinct(file_name=sys.argv[1],number_of_blocks=sys.argv[2],block_size=sys.argv[3],algorithm=sys.argv[4])
    #distinct(file_name='records.txt', number_of_blocks=4, block_size=3, algorithm='btree')