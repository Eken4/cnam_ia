import os
from datetime import datetime

from PIL import Image


class ImageProcessor:

    SAVE_LOCATION = "../../dataset"

    def __init__(self, path: str):
        self.path = path

    def process_image(self, maxsize: int) -> None:
        image = Image.open(self.path)
        width, height = image.size
        resize_ratio = min(maxsize / width, maxsize / height)
        new_size = resize_ratio * maxsize
        resized_image = image.resize((new_size, new_size))

        """ TODO : add padding"""
        """ TODO : better resize"""
        new_folder_name = datetime.now().strftime("%Y%m%d%H%M%S")
        resized_image.save(
            self.SAVE_LOCATION + "/" + new_folder_name + "/image.png"
        )

    def process_folder(self, size: int):
        urls = os.path.listdir(self.path)
        for url in urls:
            self.process_image(size, url)
        pass
