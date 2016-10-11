
class BPTree(object):
    def __init__(self, capacity):
        self._capacity = capacity
        self._tree = BPTreeLeaf([], None, self._capacity)

    def insert(self, key):
        (pkey, ppointer) = self._tree.insert(key)
        if (pkey, ppointer) != (None, None):
            self._tree = BPTreeNode([pkey], [self._tree, ppointer], self._capacity)

    def keys(self):
        # type: () -> object
        return self._tree.keys()


class BPTreeNode(object):
    def __init__(self, keys, pointers, capacity):
        self._keys = keys
        self._pointers = pointers
        self._capacity = capacity

    def keys(self):
        return self._pointers[0].keys()

    def insert_here(self, position, key, pointer):
        self._keys.insert(position, key)
        self._pointers.insert(position + 1, pointer)

        # if we are over capacity, we need to split.
        if len(self._keys) > self._capacity:

            _slicer = len(self._keys) // 2
            lower_keys = self._keys[:_slicer]
            lower_pointers = self._pointers[:_slicer + 1]

            pkey = self._keys[_slicer]

            upper_keys = self._keys[_slicer + 1:]
            upper_pointers = self._pointers[_slicer + 1:]
            ppointer = BPTreeNode(upper_keys, upper_pointers, self._capacity)
            self._keys = lower_keys
            self._pointers = lower_pointers
            return (pkey, ppointer)
        else:
            return (None, None)

    def insert(self, key):
        index = 0
        while index < len(self._keys) and key >= self._keys[index]:
            index = index + 1
        (pkey, ppointer) = self._pointers[index].insert(key)
        if (pkey, ppointer) != (None, None):
            return self.insert_here(index, pkey, ppointer)
        else:
            return (None, None)


class BPTreeLeaf(object):
    def __init__(self, keys, next_leaf, capacity):

        if len(keys) > capacity:
            raise "In sufficient message"

        self._keys = keys
        self._next = next_leaf
        self._capacity = capacity

    def keys(self):
        all_keys = []
        bucket = self
        while bucket is not None:
            all_keys.extend(bucket._keys)
            bucket = bucket._next
        return all_keys

    def insert(self, key):
        index = 0
        while index < len(self._keys) and key > self._keys[index]:
            index = index + 1
        if index < len(self._keys) and self._keys[index] == key:
            return (None, None)
        self._keys.insert(index,key)

        if len(self._keys) > self._capacity:
            _slicer = len(self._keys) // 2
            lower_keys = self._keys[:_slicer]
            upper_keys = self._keys[_slicer:]

            self._keys = lower_keys
            self._next = BPTreeLeaf(upper_keys, self._next, self._capacity)

            return (self._next._keys[0], self._next)
        else:
            return (None, None)
