from PIL import Image

input = Image.new('L', [1920, 1080])

pixel_map = input.load()
width, height = input.size

for i in range(width//2):
    for j in range(height):
        r,g,b = input.getpixel(i, j)
        grayscale = (.299*r, .587*g, .114*b)
        pixel_map[i, j] = (int(grayscale, int(grayscale, int(grayscale))))


input.save ('grayscale', format = 'png')

