import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

sample_rate, pianoC = wavfile.read('PianoC.wav')
t = np.arange(pianoC.shape[0])
freq = np.fft.fftfreq(t.shape[-1])*sample_rate
#realpianoC = pianoC.real
sp = np.fft.fft(pianoC)
print(t.shape)

plt.plot(freq, )
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Spectrum of metallica-for-whom-the-bell-tolls')
plt.xlim((0, 22000))
plt.grid()
plt.show()



