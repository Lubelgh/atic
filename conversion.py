from PIL import Image

input = Image.new("RGB", (100, 100))
pixel_map = input.load()
width, height = input.size

time = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
amplitude = (20, 40, 30, 67, 21, 98, 83, 78, 65, 68)
frequency = (440, 450, 480, 510, 430, 400, 380, 350, 450, 420)

for i in range(width):
    for j in range(height):
        pixel_map[i, j] = 255, 255, 255

for i in range(len(time)):
    for j in range(len(amplitude)):
        for k in range(len(frequency)):
            pixel_map[time[i], amplitude[j]] = (frequency[k] % 255, amplitude[j] % 255, (amplitude[j]*frequency[k]) % 255)

input.save ('converted', format = 'png')

