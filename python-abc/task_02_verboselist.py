class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        if item in self:
            super().remove(item)
            print(f"Removed [{item}] from the list.")
        else:
            print(f"[{item}] not found in the list.")

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
