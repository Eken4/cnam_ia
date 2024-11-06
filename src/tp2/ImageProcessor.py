import os
from datetime import datetime

from PIL import Image


class ImageProcessor:

    SAVE_LOCATION = "dataset"
    BACKGROUND_COLOR_RGBMODE = (114, 114, 144)
    BACKGROUND_COLOR_BWMODE = (114)

    def __init__(self, path: str):
        self.path = path

    def _resize(self, image: Image, maxsize: int) -> Image:
        width, height = image.size
        resize_ratio = min(maxsize / width, maxsize / height)
        new_width = int(width * resize_ratio)
        new_height = int(height * resize_ratio)
        return image.resize((new_width, new_height))

    def _add_padding(self,
                     image: Image, maxsize: int,
                     background_color: int | tuple[int, int, int]) -> Image:
        width, height = image.size
        if width == height:
            return image
        elif width > height:
            result = Image.new(image.mode, (width, width), background_color)
            result.paste(image, )
            return result
        else:
            result = Image.new(image.mode, (height, height), background_color)
            result.paste(image, )
            return result

    @staticmethod
    def _save_image(image: Image, path: str) -> None:
        os.makedirs(path, exist_ok=True)
        image.save(
            os.path.join(path, "image.png")
        )

    def _process_image(self, filepath: str, maxsize: int) -> None:
        print(filepath)
        image = Image.open(os.path.join(self.path, filepath))
        resized_image = self._resize(image, maxsize)
        background_color = self.BACKGROUND_COLOR_BWMODE if image.mode == 'L' \
            else self.BACKGROUND_COLOR_RGBMODE
        padded_image = self._add_padding(resized_image,
                                         maxsize,
                                         background_color)

        """ TODO : add padding"""
        """ TODO : better resize"""
        new_folder_name = datetime.now().strftime("%Y%m%d%H%M%S")
        new_location = os.path.join(self.SAVE_LOCATION, new_folder_name)
        self._save_image(padded_image, new_location)

    def process_folder(self, size: int) -> None:
        urls = os.listdir(self.path)
        for url in urls:
            self._process_image(url, size)
