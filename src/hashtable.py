class HashDict(object):
    def __init__(self,numBuckets):
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])

    def insert(self,dictKey,dictVal):
        hashBucket=self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0]==dictKey:
                hashBucket[i] = (dictKey,dictVal)
                return
        hashBucket.append((dictKey,dictVal))

    def keys(self):
        keys=[]
        for each_bucket in range(self.numBuckets):
            keys.extend([x for x,_ in self.buckets[each_bucket]])

        return sorted(keys)
    def dict(self):
        _result='{'
        for bucket in self.buckets:
               for each in bucket:
                   _result = _result + str(each[0])+':'+str(each[1])+','
        return _result[:-1]+'}'