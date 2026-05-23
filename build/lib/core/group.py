class Group:
    def __init__(self):
        self.items = []

    def add(self, *items):
        self.items.extend(items)

    def remove(self, *items):
        for item in items:
            if item in self.items:
                self.items.remove(item)

    def position(self, newx, newy):
        for item in self.items:
            item.x += newx
            item.y += newy

    def change_rgb_values(self, r, g, b):
        for item in self.items:
            item.change_rgb_values(r, g, b)

    def change_rgb_values_one(self, item, r, g, b):
        if item in self.items:
            item.change_rgb_values(r, g, b)