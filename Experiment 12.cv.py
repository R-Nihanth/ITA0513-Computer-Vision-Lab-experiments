
# Import required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

# Read image from URL
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
    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(
        image, cv2.COLOR_BGR2RGB
    )

    # Get image dimensions
    rows, cols = image_rgb.shape[:2]

    # Select three points from original image
    points1 = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    # Destination points
    points2 = np.float32([
        [10, 100],
        [200, 50],
        [100, 250]
    ])

    # Create affine transformation matrix
    matrix = cv2.getAffineTransform(
        points1, points2
    )

    # Apply affine transformation
    affine_image = cv2.warpAffine(
        image_rgb,
        matrix,
        (cols, rows)
    )

    # Display images
    plt.figure(figsize=(10, 4))

    # Original image
    plt.subplot(1, 2, 1)
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")

    # Affine transformed image
    plt.subplot(1, 2, 2)
    plt.imshow(affine_image)
    plt.title("Affine Transformed Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
