class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.levels = { # словарь в котором сохраняются списки при переходе с уровня на уровень
            0: [0, []]
        }
        self.level = 0 # обозначает уровень списка
        self.index_on_level = self.levels[self.level][0]
        

    def __iter__(self):
        self.levels[self.level][1] = self.list_of_list #сохраняем список со списками на уровень 0
        self.index_on_level -= 1
        return self


    def __next__(self):
        self.index_on_level += 1
        while self.level >= 0 and (self.index_on_level + 1) > len(self.levels[self.level][1]):
            self.level -= 1
            if self.level < 0:
                raise StopIteration
            self.index_on_level = self.levels[self.level][0]
            self.index_on_level += 1      
        else:
            self.item = self.levels[self.level][1][self.index_on_level]
            if type(self.item) == list and len(self.item) == 0:
                next(self)
            while type(self.item) == list: #если итем это список
                self.levels[self.level + 1] = [0, []] #создаем в словаре уровень выше
                self.levels[self.level + 1][1] = self.item #сохраняем текущий список в словарь на соответствующий уровень
                self.levels[self.level][0] = self.index_on_level
                self.level += 1
                self.index_on_level = 0
                self.item = self.levels[self.level][1][self.index_on_level]
            else:
                self.item = self.levels[self.level][1][self.index_on_level]       
                return self.item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()