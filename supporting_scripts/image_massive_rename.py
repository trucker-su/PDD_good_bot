import os
import time
from PIL import Image

directory = 'F:/bolat/progi/PDD/img/'
directory2 = 'F:/bolat/progi/PDD/img1/'
images = os.listdir(directory)
y = 1
for image in images:
	filename = 'img' + str(y)
	picture = directory + image
	image = Image.open(picture)
	image.save(f'{directory2}{filename}.jpeg', 'jpeg')
	y += 1


print("переименование выполняется... 3")
time.sleep(1)
print("переименование выполняется... 2")
time.sleep(1)
print("переименование выполняется... 1")
time.sleep(1)
print("ГОТОВО! @BolatMukashev")
time.sleep(1)