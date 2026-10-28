
# Import required libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np
import urllib.request

# Read input image from URL
url = "https://sm.ign.com/ign_za/cover/m/marvels-sp/marvels-spider-man-remastered_az82.jpg"

request = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(request, timeout=30) as response:
    data = response.read()

image = cv2.imdecode(
    np.frombuffer(data, dtype=np.uint8),
    cv2.IMREAD_COLOR
)

if image is None:
    print("Error: Image not found.")
else:
    # Convert image into grayscale
    gray = cv2.cvtColor(
        image, cv2.COLOR_BGR2GRAY
    )

    # Apply Sobel X direction
    sobel_x = cv2.Sobel(
        gray,
        cv2.CV_64F,
        1,
        0,
        ksize=3
    )

    # Apply Sobel Y direction
    sobel_y = cv2.Sobel(
        gray,
        cv2.CV_64F,
        0,
        1,
        ksize=3
    )

    # Convert gradients to uint8
    sobel_x = np.uint8(np.absolute(sobel_x))
    sobel_y = np.uint8(np.absolute(sobel_y))

    # Combine X and Y gradients
    sobel_combined = cv2.addWeighted(
        sobel_x, 0.5,
        sobel_y, 0.5,
        0
    )

    # Convert original image to RGB
    image_rgb = cv2.cvtColor(
        image, cv2.COLOR_BGR2RGB
    )

    # Display results
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Grayscale Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(sobel_x, cmap="gray")
    plt.title("Horizontal Edge Detection")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(sobel_combined, cmap="gray")
    plt.title("Sobel Edge Detection")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    print("Sobel Edge Detection completed successfully.")
