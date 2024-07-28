class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("Empty")
