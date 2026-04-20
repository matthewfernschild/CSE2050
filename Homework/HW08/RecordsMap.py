# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests

class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision = 0): 
        '''Initializes the record with pos, max, min, and precision'''
        self.pos = (round(pos[0]), round(pos[1]))
        self.max = max
        self.min = min
        self.precision = precision

    def add_report(self, temp): 
        '''add_report: Checks if temp is greater than max or less than min, updates the value if so.'''
        if self.max == None:
            self.max = temp
        if self.min == None:
            self.min = temp

        if temp > self.max:
            self.max = temp
        if temp < self.min:
            self.min = temp

    def __eq__(self, other): 
        '''__eq__: Check self.pos & other rounded (in affect, if 2 positions are within 70mi radius). Returns boolean value.'''
        if not isinstance(other, LocalRecord):
            return False
        return self.pos == other.pos
            
    def __hash__(self): 
        '''Returns a hash for the object based on its position'''
        return hash(self.pos)

    def __repr__(self):
        return f"Record(pos={self.pos}, max={self.max}, min={self.min})"

class RecordsMap:
    def __init__(self): 
        self._len = 0
        self._m = 4
        self._table = [None] * self._m

    def __len__(self): 
        return self._len

    def _find_slot(self, pos):
        '''Helper function to prevent collisions - ChatGPT suggested it when I didn't realize why (2,2) and (3,3) pointed to the same place'''
        idx = hash(pos) % self._m
        start = idx
        if isinstance(pos, LocalRecord):
            rounded_pos = pos.pos
        else: 
            rounded_pos = (round(pos[0]),round(pos[1]))
        while self._table[idx] is not None:
            if self._table[idx].pos == rounded_pos:
                return idx
            idx = (idx + 1) % self._m
            if idx == start:
                raise RuntimeError("Hash table is full")

        return idx

    def add_report(self, pos, temp): 
        '''allows us to add new reports to our hashmap. Indexed via the position hash'''
        # we want to use the hashed position as a key
        idx = self._find_slot(pos)

        if self._table[idx] is None:
            self._table[idx] = LocalRecord(pos, temp, temp)
            self._len += 1
        else:
            self._table[idx].add_report(temp)

        if self._len == self._m:
            self._rehash(self._m * 2)
        

    def __getitem__(self, pos): 
        '''__getitem__ is the dunder method to get an item by calling its key in square brackets []'''
        idx = self._find_slot(pos)
        if self._table[idx] is None:
            raise KeyError
        
        return (self._table[idx].min, self._table[idx].max)
  
    def __contains__(self, pos): 
        '''__contains__ dunder method checks whether or not the table has the value'''
        idx = self._find_slot(pos)
        if self._table[idx] is not None:
            return True
        return False

    def _rehash(self, m_new): 
        '''When the table is full, _rehash doubles the size of the table and rehashes all values'''
        old_table = self._table
        self._m = m_new
        self._table = [None] * self._m
        self._len = 0

        for i in old_table:
            if i is not None:
                idx = self._find_slot(i.pos)
                self._table[idx] = i
                self._len += 1


