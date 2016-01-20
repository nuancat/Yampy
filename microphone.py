"""PyAudio Example: Play a wave file."""

import pyaudio
import wave
import sys

CHUNK = 1024


wf = wave.open("rain01.wav", 'wb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
stream = p.open(format=p.get_format_from_width(2),
                channels=2,
                rate=44100,
                input=True,
                output=True)

data = wf.writeframes(CHUNK)

# read data
data = wf.readframes(CHUNK)

# play stream (3)
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(CHUNK)

# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()