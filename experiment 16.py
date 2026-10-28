
# Import required libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

# Read image from URL
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
    # Create a copy of the image
    watermark = image.copy()

    # Add watermark text
    cv2.putText(
        watermark,
        "SPIDER-MAN",
        (30, image.shape[0] - 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (255, 255, 255),
        3,
        cv2.LINE_AA
    )

    # Blend original image and watermark
    watermarked_image = cv2.addWeighted(
        image, 0.7,
        watermark, 0.3,
        0
    )

    # Convert images to RGB
    original_rgb = cv2.cvtColor(
        image, cv2.COLOR_BGR2RGB
    )

    result_rgb = cv2.cvtColor(
        watermarked_image, cv2.COLOR_BGR2RGB
    )

    # Display images
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(result_rgb)
    plt.title("Watermarked Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Save the watermarked image
    cv2.imwrite("watermarked_image.jpg", watermarked_image)

    print("Image watermarking completed successfully.")
