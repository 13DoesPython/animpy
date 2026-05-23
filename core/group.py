class Group:
    def __init__(self):
        self.items = []

    def add(self, *items):
        self.items.extend(items)

    def remove(self, *items):
        for item in items:
            if item in self.items:
                self.items.remove(item)

    def clear(self):
        self.items.clear()

    def contains(self, item):
        return item in self.items

    def find_by_color(self, r, g, b):
        return [item for item in self.items if getattr(item, 'r', None) == r and getattr(item, 'g', None) == g and getattr(item, 'b', None) == b]

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