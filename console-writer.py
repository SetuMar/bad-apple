import os
import time
import custom_ascii_converter

image_locations = None

for a, b, path in os.walk('video-frames'):
    image_locations = path

index_image = {}

for loc in image_locations:
    index_image.update({int(loc.split('e')[1].split('.')[0]):loc})

index_image = dict(sorted(index_image.items()))
sorted_image_location = index_image.values()

time.sleep(3)

for image_loc in sorted_image_location:
    full_path = 'video-frames/' + image_loc
    
    custom_ascii_converter.generate_ascii_image(full_path, 15)
    
    time.sleep(0.02)

print("VIDEO OVER. CLOSE THE CONSOLE, WEABOO")