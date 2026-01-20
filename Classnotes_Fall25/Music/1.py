import pathlib
import time
from pygame import mixer

#my_path = pathlib.Path(__file__).parent.resolve()

music = "TubePocket.mp3"

#music = f"{my_path}/{music}"
fadeout_ms = 500

mixer.init()
mixer.music.load(music)
mixer.music.play(-1)
mixer.music.fadeout(fadeout_ms)
time.sleep(fadeout_ms/1000)
time.sleep(5)

