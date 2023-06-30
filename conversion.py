from PIL import Image

from fft2 import t
from fft2 import rms_array as amp
from fft2 import thefreq_array as freq

input = Image.open('Austin.jpg')
input.convert('RGB')
pixel_map = input.load()
width, height = input.size

time = t
amplitude = amp
frequency = freq

for i in range(width):
    for j in range(height):
        pixel_map[i, j] = 255, 255, 255

for i in range(len(time)):
    for j in range(len(amplitude)):
        for k in range(len(frequency)):
            pixel_map[int(time[i]), int(amplitude[j])] = (int(frequency[k]) % 255, int(amplitude[j]) % 255, (int(amplitude[j]*frequency[k])) % 255)

input.save ('converted', format = 'png')
