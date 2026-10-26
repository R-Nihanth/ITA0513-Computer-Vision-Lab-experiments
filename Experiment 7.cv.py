
# Import required libraries
import cv2
import matplotlib.pyplot as plt
import urllib.request
import numpy as np

# Read image from URL
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
    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(
        image, cv2.COLOR_BGR2RGB
    )

    # Get image dimensions
    height, width = image.shape[:2]

    # Increase image size
    large_image = cv2.resize(
        image_rgb,
        (width * 2, height * 2),
        interpolation=cv2.INTER_LINEAR
    )

    # Decrease image size
    small_image = cv2.resize(
        image_rgb,
        (width // 2, height // 2),
        interpolation=cv2.INTER_AREA
    )

    # Display images
    plt.figure(figsize=(12, 4))

    # Original image
    plt.subplot(1, 3, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    # Enlarged image
    plt.subplot(1, 3, 2)
    plt.imshow(large_image)
    plt.title("Enlarged Image")
    plt.axis("off")

    # Reduced image
    plt.subplot(1, 3, 3)
    plt.imshow(small_image)
    plt.title("Reduced Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    print("Image scaling completed successfully.")
