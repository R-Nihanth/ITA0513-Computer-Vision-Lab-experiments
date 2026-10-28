
# Import required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

# Read image from URL
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScGTq1Dowzv6bJUPgvMdwjmH617ZAkXpnRdRTMWZ3ylA&s=10"

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
    # Convert image to RGB
    image_rgb = cv2.cvtColor(
        image, cv2.COLOR_BGR2RGB
    )

    # Convert image into grayscale
    gray = cv2.cvtColor(
        image, cv2.COLOR_BGR2GRAY
    )

    # Convert grayscale image to float32
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    corners = cv2.cornerHarris(
        gray, 2, 3, 0.04
    )

    # Mark detected corners
    result = image_rgb.copy()
    result[corners > 0.01 * corners.max()] = [255, 0, 0]

    # Display result
    plt.figure(figsize=(8, 4))
    plt.imshow(result)
    plt.title("Harris Corner Detection")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

    print("Harris Corner Detection completed successfully.")
