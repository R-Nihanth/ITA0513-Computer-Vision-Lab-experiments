
import cv2
import matplotlib.pyplot as plt
import urllib.request
import numpy as np

# Thor image URL
url = "https://thumb.wikimedia.org/wikipedia/en/thumb/3/3c/Chris_Hemsworth_as_Thor.jpg/250px-Chris_Hemsworth_as_Thor.jpg"

try:
    # Download the image
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(request, timeout=20) as response:
        data = response.read()

    # Read image using OpenCV
    image = cv2.imdecode(
        np.frombuffer(data, dtype=np.uint8),
        cv2.IMREAD_COLOR
    )

    if image is None:
        print("Error: Unable to read image.")
    else:
        # Convert image to grayscale
        gray_image = cv2.cvtColor(
            image, cv2.COLOR_BGR2GRAY
        )

        # Apply Gaussian Blur
        blur_image = cv2.GaussianBlur(
            gray_image, (5, 5), 0
        )

        # Apply Canny Edge Detection
        edges = cv2.Canny(
            blur_image, 100, 200
        )

        # Display images
        plt.figure(figsize=(10, 4))

        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.title("Original Image")
        plt.axis("off")

        plt.subplot(1, 2, 2)
        plt.imshow(edges, cmap="gray")
        plt.title("Canny Edge Image")
        plt.axis("off")

        plt.tight_layout()
        plt.show()

        print("Canny Edge Detection completed successfully.")

except Exception as error:
    print("Error downloading image:", error)
