
# Import required libraries
import cv2
import matplotlib.pyplot as plt
import urllib.request
import numpy as np

# Read image from URL
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNoE1DISBu-GA9t0dR9G-vgfaNRrABqqdeSJ1JKRK_Aw&s=10"

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
    # Convert BGR channels
    blue_channel = image[:, :, 0]
    green_channel = image[:, :, 1]
    red_channel = image[:, :, 2]

    # Calculate histograms
    blue_hist = cv2.calcHist(
        [blue_channel], [0], None, [256], [0, 256]
    )

    green_hist = cv2.calcHist(
        [green_channel], [0], None, [256], [0, 256]
    )

    red_hist = cv2.calcHist(
        [red_channel], [0], None, [256], [0, 256]
    )

    # Plot histograms
    plt.figure(figsize=(10, 5))

    plt.plot(blue_hist, label="Blue Channel")
    plt.plot(green_hist, label="Green Channel")
    plt.plot(red_hist, label="Red Channel")

    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()
