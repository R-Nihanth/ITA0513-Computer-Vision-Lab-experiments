
# Import required libraries
import cv2
import matplotlib.pyplot as plt
import urllib.request
import numpy as np

# Image URL
url = "https://assets.epuzzle.info/puzzle/133/039/original.jpg"

try:
    # Download image
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        image_data = response.read()

    # Read image using OpenCV
    image = cv2.imdecode(
        np.frombuffer(image_data, dtype=np.uint8),
        cv2.IMREAD_COLOR
    )

    if image is None:
        print("Error: Unable to read image.")
    else:
        # Convert image to grayscale
        gray_image = cv2.cvtColor(
            image, cv2.COLOR_BGR2GRAY
        )

        # Apply Histogram Equalization
        equalized_image = cv2.equalizeHist(gray_image)

        # Display original and enhanced images
        plt.figure(figsize=(10, 4))

        plt.subplot(1, 2, 1)
        plt.imshow(gray_image, cmap="gray")
        plt.title("Original Image")
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.imshow(equalized_image, cmap="gray")
        plt.title("Equalized Image")
        plt.axis("off")

        plt.tight_layout()
        plt.show()

        # Display histograms
        plt.figure(figsize=(10, 4))

        plt.subplot(1, 2, 1)
        plt.hist(gray_image.ravel(), 256, [0, 256])
        plt.title("Original Histogram")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Frequency")

        plt.subplot(1, 2, 2)
        plt.hist(equalized_image.ravel(), 256, [0, 256])
        plt.title("Equalized Histogram")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Frequency")

        plt.tight_layout()
        plt.show()

        print("Histogram Equalization completed successfully.")

except Exception as error:
    print("Error downloading or processing image:", error)
