from .coords import Coords

class Keyframe:
    def __init__(self, pos: Coords):
        self.pos = pos

class KeyChains:
    def __init__(self, *keyframes):
        self.keyframe_list = list(keyframes)

    def follow_path(self, obj, speed=1):
        if self.keyframe_list:
            target = self.keyframe_list[0].pos # Get the FIRST one
            obj.slide_to_pos(target, speed)

            # If we reached the target, remove it to start moving to the next
            if int(obj.x) == target.x and int(obj.y) == target.y:
                self.keyframe_list.pop(0)