from iteration_utilities import deepflatten as df

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, list_object, start=-1):
        self.list_object = list_object
        self.flattenlist = list(df(self.list_object))
        self.max = len(self.flattenlist)
        self.counter = start

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        while self.counter < self.max:
            return self.flattenlist[self.counter]
        else:
            raise StopIteration


def flat_generator(list_object):
    flat_obj = (n for n in list(df(list_object)))
    return flat_obj


if __name__ == '__main__':

    flat_list = [item for item in FlatIterator(nested_list)]
    for item in flat_list:
        print(item)

    print('-'*20)

    for item in flat_generator(nested_list):
        print(item)
