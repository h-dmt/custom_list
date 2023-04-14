class CustomList:
    def __init__(self, *text):
        self.text = text
        self.c_list = self.create_list()

    def size(self):
        return len(self.text)

    def create_list(self):
        list_size = self.size()
        cust_list = [""] * list_size
        for i in range(list_size):
            cust_list[i] = self.text[i]

        return cust_list

    def append(self, value):
        old_size = len(self.c_list)
        size_new_list = old_size + 1
        new_list = [''] * size_new_list
        new_list[:old_size] = self.c_list
        new_list[size_new_list - 1] = value
        self.c_list = new_list

        return new_list

    def remove(self, index: int):
        try:
            remove_value = self.c_list[index]

        except IndexError:
            raise IndexError

        self.c_list[index] = ''
        self.c_list = self.c_list[:index] + self.c_list[index + 1:]

        return remove_value

    def get(self, index):
        try:
            value = self.c_list[index]

        except IndexError:
            raise IndexError

        return value

    def extend(self, iterable):
        old_size = len(self.c_list)
        size_new_list = old_size + len(iterable)
        new_list = [''] * size_new_list
        new_list[:old_size] = self.c_list
        new_list[old_size:] = iterable
        self.c_list = new_list

        return new_list

    def insert(self, index, value):
        try:
            self.c_list[index] = value
        except IndexError:
            raise IndexError("invalid index")

        return self.c_list

    def pop(self):
        removed_value = self.c_list[-1]
        size = len(self.c_list)
        self.c_list = self.c_list[:size - 1]

        return removed_value

    def clear(self):
        self.c_list = []

    def index(self, value):
        for idx, v in enumerate(self.c_list):
            if v == value:
                return idx

        raise ValueError(f"'{value}' not in custom list")

    def count(self, value):
        counter = 0
        for v in self.c_list:
            if v == value:
                counter += 1

        return counter

    def reverse(self):
        return self.c_list[::-1]

    def copy(self):
        value = ""
        for v in self.c_list:
            value += v

        return CustomList(value)

    def add_first(self, value):
        self.c_list = [value] + self.c_list

    # noinspection SpellCheckingInspection
    def dictionize(self):
        dct = {}
        for idx, v in enumerate(self.c_list):
            if idx % 2 == 0:
                key = v
                if idx + 1 >= len(self.c_list):
                    dct[v] = ' '
                    return dct
                dct[v] = self.c_list[idx + 1]

        return dct

    def move(self, amount):

        return self.c_list[amount:] + self.c_list[:amount]

    def sum(self):
        n = 0
        for value in self.c_list:
            if isinstance(value, int):
                n += value
            else:
                n += len(value)

        return n

    # noinspection SpellCheckingInspection
    def overbound(self):
        biggest = self.c_list[0] if isinstance(self.c_list[0], int) else len(self.c_list[0])
        idx_biggest = 0

        for idx, el in enumerate(self.c_list):
            if isinstance(el, int):
                if int(el) > biggest:
                    biggest = int(el)
                    idx_biggest = idx
            else:
                if len(el) > biggest:
                    biggest = len(el)
                    idx_biggest = idx

        return idx_biggest

    # noinspection SpellCheckingInspection
    def underbound(self):
        smallest = self.c_list[0] if isinstance(self.c_list[0], int) else len(self.c_list[0])
        idx_smalles = 0

        for idx, el in enumerate(self.c_list):
            if isinstance(el, int):
                if int(el) < smallest:
                    smallest = int(el)
                    idx_smalles = idx
            else:
                if len(el) < smallest:
                    smallest = len(el)
                    idx_smalles = idx

        return idx_smalles

    def __str__(self):
        return f"{self.c_list}"
