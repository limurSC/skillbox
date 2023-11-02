class DoubleElement:
    def __init__(self, *lst):
        self.elements = list(lst)
        self.index = 0

    def __next__(self):
        if self.index < len(self.elements) - 1:
            result = (self.elements[self.index], self.elements[self.index + 1])
            self.index += 2
            return result
        elif self.index == len(self.elements) - 1:
            result = (self.elements[self.index], None)
            self.index += 2
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)    
