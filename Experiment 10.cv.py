
# Import required libraries
import cv2
import matplotlib.pyplot as plt
import urllib.request
import numpy as np

# Read input image from URL
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIUTsK3Hyrx-WGhHIFN_QOvyJtOq3ZPhXV5wtCsQBufjjVM_-JFl51a0g&s=10"

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
    # Convert BGR image to RGB
    image_rgb = cv2.cvtColor(
        image, cv2.COLOR_BGR2RGB
    )

    # Rotate image 90 degrees clockwise
    rotated_image = cv2.rotate(
        image_rgb,
        cv2.ROTATE_90_CLOCKWISE
    )

    # Display images
    plt.figure(figsize=(10, 4))

    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    # Rotated image
    plt.subplot(1, 2, 2)
    plt.imshow(rotated_image)
    plt.title("90 Degree Clockwise Rotation")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
