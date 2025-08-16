import os
from tkinter.font import names

from PIL import Image

def load_imgs(folder_path):
    imgs = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            if img is not None:
                name = filename.split('.')[0]
                imgs[name] = img
            else:
                print(f"警告：无法加载图片{filename}")
    return imgs