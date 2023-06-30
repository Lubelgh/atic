# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
from scipy.io import wavfile
import pandas as pnd
from matplotlib import pyplot as plt
import scipy as scip
import librosa
import random
import operator
chunk = 1024

# open up a wave

wf = wave.open('music.wav')
swidth = wf.getsampwidth()
RATE = wf.getframerate()
# use a Blackman window
window = np.blackman(chunk)
# open stream
p = pyaudio.PyAudio()
channels = wf.getnchannels()
stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = channels,
                rate = RATE,
                output = True)
thefreq_list = []
# read some data
data = wf.readframes(chunk)
# play stream and find the frequency of each chunk
print('switdth {} chunk {} data {} ch {}'.format(swidth,chunk,len(data), channels))
while len(data) == chunk*swidth*channels:
    # write data out to the audio stream
    #stream.write(data)
    # unpack the data and times by the hamming window
#    indata = np.array(wave.struct.unpack("%dh"%(len(data)/(swidth)),data))*window
    indata = np.fromstring(data, dtype='int32')
    # deinterleave, select 1 channel
    channel0 = indata[0::channels]
    # Take the fft and square each value
    fftData=abs(np.fft.rfft(indata))**2
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
        print ("The freq is %f Hz." % (thefreq))
        thefreq_list.append (thefreq)
    else:
        thefreq = which*RATE/chunk
        print ("The freq is %f Hz." % (thefreq))
        thefreq_list.append(thefreq)
    # read some more data
    data = wf.readframes(chunk)
if data:
   stream.write(data)
stream.close()
p.terminate()
print (thefreq.shape)
sample_rate, song = wavfile.read('music.wav')
t = np.arange(0, len(thefreq_list))
print(t)
thefreq_array = np.array(thefreq_list)
freq = scip.fft.fftfreq(t.shape[-1])*sample_rate
realsong = abs(song.real)
print(freq)
#y  = scip.fft.fft(realsong)
#print (y)
print(song)


#length = song.shape [0]/ sample_rate
#time = np.linspace(0., length, song.shape[0])
#plt.plot(time, song)
#plt.legend()
#plt.xlabel('Time (s)')
#plt.ylabel('Amplitude')
#plt.show()
#print (song.shape)
#array_song = np.array(song)
#rarray_song = array_song.flatten()
#new_rarray = np.array_split(rarray_song, 2)
#a = new_rarray[0]
audio = 'music.wav'
x, sr = librosa.load(audio)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
#Xdb_one_d = Xdb.flatten ()
#print (Xdb_one_d.shape)
#print (Xdb_one_d.shape)
#print (t.shape)
#print (thefreq.shape)
#indeces = np.array(range(len(Xdb_one_d)))
#remove = np.random.permutation(len(Xdb_one_d))[:len(thefreq_array)]
#selected = np.in1d(indeces, remove, assume_unique=True)
#Xdb_one_d_shortened = Xdb_one_d[selected]
#list_Xdb =Xdb.tolist()
#list_Xdb2 = list_Xdb [1]
#list_Xdb2 = list_Xdb2 [: -1]
#amplitude_in_db = np.array(list_Xdb2)
#print (amplitude_in_db.shape)
#print (thefreq_array.shape)
#Xdb_array = Xdb.reshape (1, len(thefreq_array))
#print (Xdb_array)
#t_list = t.tolist ()

#t = np.arange(0, len(amplitude_in_db))
plt.figure(figsize=(15,3))
librosa.display.specshow(Xdb, sr=sr, x_axis='time',y_axis='hz')
plt.colorbar()
S, phase = librosa.magphase(librosa.stft(x))
rms = librosa.feature.rms(S=S)

fig, ax = plt.subplots(nrows=2, sharex=True)
times = librosa.times_like(rms)
ax[0].semilogy(times, rms[0], label='RMS Energy')
ax[0].set(xticks=[])
ax[0].legend()
ax[0].label_outer()

librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),
        y_axis='log', x_axis='time', ax=ax[1])

ax[1].set(title='log Power spectrogram')
print(rms)
rms_array = np.array(rms)
print (rms.shape)
print(t)

print(rms_array.T.shape)
print (rms_array[0].shape)
rms_list = list(rms_array[0])
rms_list.remove(0.00000000e+00)
#rms_list.remove(0.00000000e+00)
rms_array = np.array(rms_list)

df = pnd.DataFrame({
   #"Point in time" : np.array(t),
   "Amplitude" :     rms_array,
    "Frequency" :    thefreq_array,
    "time"      :    t

})
print(df)
print(t.shape)
plt.plot (t, thefreq_array)
plt.title ("kek")
plt.show()