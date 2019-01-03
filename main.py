import numpy as np
import math
import scipy.io.wavfile

fs = 44100; #hz
freq = 1000;
wave = 2*math.pi*freq * np.array(list(range(1, fs + 1))) / fs
tones = np.asarray([math.sin(x) for x in wave])

scipy.io.wavfile.write('test.wav',fs,tones)