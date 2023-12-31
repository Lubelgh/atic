import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import scipy
x = np.linspace(1, 100, 100)
y = x*x

def get_piano_notes():
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B']
    base_freq = 440  # Frequency of Note A4
    keys = np.array([x + str(y) for y in range(0, 9) for x in octave])
    # Trim to standard 88 keys
    start = np.where(keys == 'A0')[0][0]
    end = np.where(keys == 'C8')[0][0]
    keys = keys[start:end + 1]

    note_freqs = dict(zip(keys, [2 ** ((n + 1 - 49) / 12) * base_freq for n in range(len(keys))]))
    return note_freqs



def get_sine_wave(frequency, duration, sample_rate=44100, amplitude=4096):
    t = np.linspace(0, duration, int(sample_rate*duration)) # Time axis
    wave = amplitude*np.sin(2*np.pi*frequency*t)
    return wave

# Get middle C frequency
note_freqs = get_piano_notes()
frequency = note_freqs['C4']

# Pure sine wave
sine_wave = get_sine_wave(frequency, duration=2, amplitude=2048)
wavfile.write('pure_c.wav', rate = 44100, data = sine_wave.astype(np.int16))

# Load data from wav file
sample_rate, PianoC = wavfile.read('PianoC.wav')
plt.style.use('seaborn-dark')
# Plot sound wave
plt.plot(PianoC[100:4500])
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sound Wave of Middle C on Piano')
plt.grid()
plt.show()