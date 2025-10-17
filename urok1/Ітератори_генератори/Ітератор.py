class Counter:
    def __init__(self, max_number):
        self.current = 0
        self.max_number = max_number
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.max_number:
            result = 2 ** self.current
            self.current += 1
            return result
        else:
            raise StopIteration
        
counter = Counter(10)
for number in counter:
    print(number)


    












