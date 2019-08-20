import time, sys
from pygame import mixer
mixer.init()

sound = mixer.Sound('song.wav')
sound.play()

time.sleep(sound.get_length()+1) 