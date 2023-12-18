import types

def flat_generator(list_of_lists):
    levels = { # словарь в котором сохраняются списки при переходе с уровня на уровень
    0: [0, []]
    }
    level = 0 # обозначает уровень списка
    index_on_level = levels[level][0]
    levels[level][1] = list_of_lists #сохраняем список со списками на уровень 0
    index_on_level -= 1
    while levels[0][0] != len(list_of_lists):
        index_on_level += 1
        while level >= 0 and (index_on_level + 1) > len(levels[level][1]):
            level -= 1
            if level < 0:
                return
            index_on_level = levels[level][0]
            index_on_level += 1      
        else:
            item = levels[level][1][index_on_level]
            if type(item) == list and len(item) == 0:
                exit()
            while type(item) == list: #если итем это список
                levels[level + 1] = [0, []] #создаем в словаре уровень выше
                levels[level + 1][1] = item #сохраняем текущий список в словарь на соответствующий уровень
                levels[level][0] = index_on_level
                level += 1
                index_on_level = 0
                item = levels[level][1][index_on_level]
            else:
                item = levels[level][1][index_on_level]
                print(item)      
                yield item


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()