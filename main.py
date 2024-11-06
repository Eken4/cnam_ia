from src.tp2.ImageProcessor import ImageProcessor


def main():

    input_folder = "images/input"
    image_size = 640

    processor = ImageProcessor(input_folder)
    processor.process_folder(image_size)


if __name__ == "__main__":
    main()
