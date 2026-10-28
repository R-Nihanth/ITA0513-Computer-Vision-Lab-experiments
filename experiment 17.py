
# Import required libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np
import urllib.request

# Read image from URL
url = "https://cdn-fastly.motorcycle.com/media/2026/09/16/18262/2027-kawasaki-ninja-h2-announced-for-europe.jpg?size=720x845&nocrop=1"

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
    # Resize image to ensure sufficient dimensions
    image = cv2.resize(image, (500, 500))

    # Create a copy of original image
    original = image.copy()

    # Select Region of Interest (ROI)
    roi = image[50:200, 50:200].copy()

    # Copy and paste ROI to another location
    image[250:400, 250:400] = roi

    # Display images
    plt.figure(figsize=(12, 4))

    # Original image
    plt.subplot(1, 3, 1)
    plt.imshow(
        cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
    )
    plt.title("Original Image")
    plt.axis("off")

    # Cropped image
    plt.subplot(1, 3, 2)
    plt.imshow(
        cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    )
    plt.title("Cropped Image")
    plt.axis("off")

    # Copy and pasted image
    plt.subplot(1, 3, 3)
    plt.imshow(
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    )
    plt.title("Copy and Pasted Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    print("ROI operation completed successfully.")
