class Heap:
    def __init__(self, capacity):
        self.items = [0] * capacity
        self.size = 0
        self.capacity = capacity

    def print_items(self):
        print(f"items = {self.items}")

    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        self.items[index_one], self.items[index_two] = \
            self.items[index_two], self.items[index_one]

    def ensure_extra_capacity(self):
        # print(f"{self.capacity=}")
        # print(f"{self.size=}")
        if self.size == self.capacity:
            self.items.extend([0] * self.capacity * 2)
            self.capacity *= 2

    def peek(self):
        if self.size == 0:
            print("No Elements!!!")
        else:
            return self.items[0]

    def poll(self):
        if self.size == 0:
            print("No Elements!!!")
        else:
            item = self.items[0]
            self.items[0] = self.items[self.size - 1]
            self.items[self.size - 1] = 0
            self.size -= 1
            self.heapify_down()
            return item

    def add(self, item):
        self.ensure_extra_capacity()
        self.items[self.size] = item
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]: # noqa
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and \
                    self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)

            index = smaller_child_index


obj = Heap(10)
obj.add(10)
obj.add(15)
obj.add(20)
obj.add(17)
obj.add(25)
obj.print_items()
obj.poll()
obj.print_items()
