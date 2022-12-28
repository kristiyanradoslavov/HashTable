class HashTable:

    def __init__(self):
        self.capacity = 4
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def __getitem__(self, item):
        try:
            index = self.keys.index(item)
            return self.values[index]

        except ValueError:
            raise KeyError(item)

    def __setitem__(self, key, value):
        if self.full_capacity():
            self.keys = self.keys + [None] * self.capacity
            self.values = self.values + [None] * self.capacity
            self.capacity = len(self.keys)

        current_index = self.__encrypt(key)
        if self.keys[current_index] is not None:
            current_index = self.__replace(current_index)

        self.keys[current_index] = key
        self.values[current_index] = value

    def __encrypt(self, key):
        return sum(ord(k) for k in str(key)) % self.capacity

    def __replace(self, index):
        if index >= self.capacity:
            index = 0

        if self.keys[index] is None:
            return index

        return self.__replace(index + 1)

    def full_capacity(self):
        result = [x for x in self.keys if x is None]
        if len(result) == 0:
            return True
        else:
            return False

    def get(self, item):
        try:
            index = self.keys.index(item)
            return self.values[index]

        except ValueError:
            return None

    def __len__(self):
        return len([x for x in self.keys if x is not None])

    def add(self, key, value):
        self.__setitem__(key, value)




table = HashTable()

table["name"] = "Peter"
table["age"] = 25
table["color"] = "blue"
table["diet"] = "keto"
table["something"] = "else"
table["newggg"] = "one"
table["newah"] = "onew"
table["newsj"] = "onec"
table["newj"] = "onex"
table["newo"] = "onez"
table["new"] = "oneb"
table["newq"] = "onem"
table["news"] = "oner"
table.add(5, "five")

print(table)

print(table.get("namez"))
print(table["age"])
print(len(table))
