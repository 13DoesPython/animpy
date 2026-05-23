from .coords import Coords

class Keyframe:
    def __init__(self, pos: Coords):
        self.pos = pos

    def set_pos(self, pos: Coords):
        self.pos = pos

    def distance_to(self, other):
        if isinstance(other, Keyframe):
            return self.pos.distance_to(other.pos)
        return self.pos.distance_to(other)

class KeyChains:
    def __init__(self, *keyframes):
        self.keyframe_list = list(keyframes)

    def append(self, keyframe):
        self.keyframe_list.append(keyframe)

    def clear(self):
        self.keyframe_list.clear()

    def reverse_path(self):
        self.keyframe_list.reverse()

    @property
    def is_complete(self):
        return len(self.keyframe_list) == 0

    def follow_path(self, obj, speed=1):
        if self.keyframe_list:
            target = self.keyframe_list[0].pos
            obj.slide_to_pos(target, speed)

            # If we reached the target, remove it to start moving to the next
            if int(obj.x) == target.x and int(obj.y) == target.y:
                self.keyframe_list.pop(0)
