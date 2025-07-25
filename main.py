import uuid
import os
import cv2
from matplotlib import pyplot as plt

ANC_PATH = "anchor"
POS_PATH = "positive"

os.makedirs(ANC_PATH, exist_ok=True)
os.makedirs(POS_PATH, exist_ok=True)

cap = cv2.VideoCapture(0)
last_frame = None  # To store last frame

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting...")
        break

    # Cut down frame to 250x250px (center crop)
    frame = frame[120:120+250, 200:200+250, :]

    # Show the frame
    cv2.imshow('Webcam Test', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('a'):
        img_name = os.path.join(ANC_PATH, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(img_name, frame)
        print(f"Saved anchor image: {img_name}")

    elif key == ord('p'):
        img_name = os.path.join(POS_PATH, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(img_name, frame)
        print(f"Saved positive image: {img_name}")

    elif key == ord('q'):
        break

    last_frame = frame.copy()

cap.release()
cv2.destroyAllWindows()

# Display the last captured frame using matplotlib
if last_frame is not None:
    rgb_frame = cv2.cvtColor(last_frame, cv2.COLOR_BGR2RGB)
    plt.imshow(rgb_frame)
    plt.title("Last Captured Frame")
    plt.axis('off')
    plt.show()
else:
    print("No frame was captured.")
