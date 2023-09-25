import os
import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt


def main():
    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        raise FileNotFoundError(image_path)

    image = cv2.imread(image_path, 0)

    img_hist, _ = np.histogram(np.array(image).flatten(), bins=np.arange(256 + 1))

    plt.plot(img_hist)

    plt.title("Image Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    output_file_path = os.path.join(os.path.dirname(image_path), "histogram.png")
    plt.savefig(output_file_path)


if __name__ == "__main__":
    main()
