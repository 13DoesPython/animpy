import time
from pygame import mixer

class Audio:
    def __init__(self):
        mixer.init()
        self.sounds = {}
        self.channels = {}

    def load(self, name, file_path):
        self.sounds[name] = mixer.Sound(file_path)

    def play(self, name, loop=0):
        if name in self.sounds:
            self.channels[name] = self.sounds[name].play(loops=loop)

    def stop_all(self):
        mixer.stop()

    def is_playing(self, name=None):
        if name is None:
            return mixer.get_busy()
        if name in self.channels:
            return self.channels[name].get_busy()
        return False

    def set_volume(self, name, volume):
        if name in self.sounds:
            self.sounds[name].set_volume(volume)

    def stop(self, name):
        if name in self.channels:
            self.channels[name].stop()

    def pause(self, name):
        if name in self.channels:
            self.channels[name].pause()

    def resume(self, name):
        if name in self.channels:
            self.channels[name].unpause()

    def fade_out(self, name, duration):
        if name in self.channels:
            self.channels[name].fadeout(int(duration * 1000))

    def fade_in(self, name, duration, loop=0):
        if name in self.sounds:
            self.channels[name] = self.sounds[name].play(loops=loop, fade_ms=int(duration * 1000))

    def play_for_time(self, name, duration):
        if name in self.sounds:
            self.sounds[name].play()
            time.sleep(duration)
            self.sounds[name].stop()
