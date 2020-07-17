class RingBuffer:
    def __init__(self, capacity, data = []):
        self.capacity = capacity
        self._data = list(data)[-capacity:]
        self.index = 0 

    def append(self, item):
        if len(self._data) == self.capacity:
            self._data[self.index] = item
        else:
            self._data.append(item)
        self.index = (self.index + 1) % self.capacity

    def get(self):
        return self._data