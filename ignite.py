import os

# Set the log level to 'OFF' to hide the camera warnings
os.environ["OPENCV_LOG_LEVEL"] = "OFF"
import cv2
import BCJA

print("--- STARTING ENGINE ---")

# 1. Load the video
video_path = "test.mp4"
cap = cv2.VideoCapture(video_path)

# 2. Check if video exists
if not cap.isOpened():
    print("Error: Could not open test.mp4")
    exit()

print("Video loaded successfully. Launching AI...")

# 3. Run the Head Pose logic (detected in your screenshot)
# 3. Run the Head Pose logic
try:
    # Run the main engine
    BCJA.head_pose(cap)

except KeyboardInterrupt:
    # This runs when you press Ctrl+C
    print("\n\n--------------------------------------------------")
    print("🛑 ENGINE STOPPED BY USER.")
    print("   Data logs saved.")
    print("   Goodbye!")
    print("--------------------------------------------------\n")
