# Определите класс итератор ReverseIter, который принимает список и итерируется
# по нему в обратном направлении

class ReverseIter:
    def __init__(self, seq):
        self.seq = seq

    def __iter__(self):
        self.a = len(self.seq)-1
        return self

    def __next__(self):
        if self.a >= 0:
            x = self.seq[self.a]
            self.a -= 1
            return x
        else:
            raise StopIteration


numbers = [10, 'wow', 11, 12, 13, 14, 'yep', 15]
my_numb = ReverseIter(numbers)
for i in my_numb:
    print(i)
