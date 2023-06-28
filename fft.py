import numpy as np
import scipy as scip
from scipy.io import wavfile
import matplotlib.pyplot as plt
import pandas as pnd

sample_rate = 44100
duration = 309
sample_rate, song = wavfile.read('pure_c.wav')
t = np.arange(song.shape[0])
print(t)
freq = scip.fft.fftfreq(t.shape[-1])*sample_rate
realsong = abs(song.real)
print(freq)
y  = scip.fft.fft(realsong)
print (y)
print(song)


#length = song.shape [0]/ sample_rate
#time = np.linspace(0., length, song.shape[0])
#plt.plot(time, song)
#plt.legend()
#plt.xlabel('Time (s)')
#plt.ylabel('Amplitude')
#plt.show()
#print (song.shape)
array_song = np.array(song)
rarray_song = array_song.flatten()
new_rarray = np.array_split(rarray_song, 2)
a = new_rarray[0]



df = pnd.DataFrame({
   "Point in time" : np.array(t),
   "Amplitude" :     abs(a),
    "Frequency" :     np.array(freq)

})
print(df)
print(rarray_song.shape)
print(t.shape)
plt.plot (abs(freq), abs(a))
plt.title ("kek")
plt.show()