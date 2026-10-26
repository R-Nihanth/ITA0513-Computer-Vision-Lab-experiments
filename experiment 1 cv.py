import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter as tk

# Select image
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
)

# Read image
image = cv2.imread(file_path)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Gray Scale Image")
plt.axis("off")

plt.show()
