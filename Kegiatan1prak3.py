class Stack:
    def _init_(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def reverse_string(input_string):
    stack = Stack()
    for char in input_string:
        stack.push(char)

    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


input_string = input("Masukkan string: ")
reversed_string = reverse_string(input_string)

print("String terbalik: ", reversed_string)