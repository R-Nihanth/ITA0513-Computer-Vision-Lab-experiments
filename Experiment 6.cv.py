
# Import OpenCV library
import cv2

# Read video file
video = cv2.VideoCapture("C:/Users/nihan/Downloads/Power star veido.mp4")

# Check video availability
if not video.isOpened():
    print("Error opening video")
else:
    print("Press 's' for slow motion")
    print("Press 'f' for fast motion")
    print("Press 'n' for normal speed")
    print("Press 'q' to exit")

    # Read video frames
    while True:
        ret, frame = video.read()

        if not ret:
            break

        # Display normal video
        cv2.imshow("Video Processing", frame)

        # Control video speed
        key = cv2.waitKey(30) & 0xFF

        if key == ord('s'):
            cv2.waitKey(200)

        elif key == ord('f'):
            # Skip additional frames for fast motion
            video.set(
                cv2.CAP_PROP_POS_FRAMES,
                video.get(cv2.CAP_PROP_POS_FRAMES) + 3
            )

        elif key == ord('n'):
            pass

        elif key == ord('q'):
            break

    # Release resources
    video.release()
    cv2.destroyAllWindows()
