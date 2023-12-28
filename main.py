from itertools import chain


class FlatIterator:
    def __init__(self, list):
        self.main_list = list

    def __iter__(self):
        self.main_cursor = 0
        self.nested_cursor = -1
        return self

    def __next__(self):
        self.nested_cursor += 1
        if self.nested_cursor == len(self.main_list[self.main_cursor]):
            self.main_cursor += 1
            self.nested_cursor = 0
            if self.main_cursor == len(self.main_list):
                raise StopIteration
        return self.main_list[self.main_cursor][self.nested_cursor]


def flat_generator(main_list):
    for mail_item in main_list:
        for item in mail_item:
            yield item


def flat_generator_recurse(main_list):
    for main_item in main_list:
        if isinstance(main_item, list):
            for sub_item in flat_generator_recurse(main_item):
                yield sub_item
        else:
            yield main_item



if __name__ == '__main__':

    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    print('-'*8)


    for item in flat_generator(nested_list):
        print(item)

    gen_nested_list = (x for l in nested_list for x in l)
    print(tuple(gen_nested_list))
    print('-' * 8)


    nested_list6 = [
        ['a', ['b', ['c']], 'd'],
        ['e', ['f', ['h', ['j', [False]], 1]]],
        [2, 3, None], [[[4]]]
    ]

    for item in flat_generator_recurse(nested_list6):
        print(item)