
# Import required libraries
import cv2
import matplotlib.pyplot as plt
import urllib.request
import numpy as np

# Read input image
url = "https://cdn.bikedekho.com/upload/userreviewimages/6a813b42e2a4e.jpeg"

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

    # Rotate image 270 degrees clockwise
    rotated_image = cv2.rotate(
        image_rgb,
        cv2.ROTATE_90_COUNTERCLOCKWISE
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
    plt.title("270 Degree Clockwise Rotation")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
