# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests

class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision = 0): 
        '''Initializes the record with pos, max, min, and precision'''
        self.pos = pos
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
        p0 = round(self.pos[0])
        p1 = round(self.pos[1])

        if p0 == round(other[0]) and p1 == (other[1]):
            return True
        return False
        
    def __hash__(self): 
        '''Returns a hash for the object based on its position'''
        return hash(self.pos)

    def __repr__(self):
        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"

class RecordsMap:
    def __init__(self): 
        self._len = 0
        self.min = 0
        self.max = 0
    
    def __len__(self): 
        return self._len

    def add_report(self, pos, temp): pass

    def __getitem__(self, pos): pass
  
    def __contains__(self, pos): pass

    def _rehash(self, m_new): pass