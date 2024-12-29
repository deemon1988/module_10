import multiprocessing as mp
import os
from queue import Empty

from PIL import Image

def resize_image(image_paths, queue):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((800, 600))
        queue.put((image_path, image))

def change_color(queue):
    while True:
        try:
            image_path, image = queue.get(timeout=1)
        except Empty:
            break
        image = image.convert('L')
        image.save(f'./re_images/{image_path.replace('./images/', '')}')

if __name__ == '__main__':
    data = []
    queue = mp.Queue()

    dir = os.getcwd() + '/images'
    images_titles = [name for name in os.listdir(dir)]
    print(images_titles)


    for image in images_titles:
        data.append(f'./images/{image}')

    resize_process = mp.Process(target=resize_image, args=(data, queue))
    change_process = mp.Process(target=change_color, args=(queue,))

    resize_process.start()
    change_process.start()

    resize_process.join()
    change_process.join()