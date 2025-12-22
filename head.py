import config
import os
from drowsiness import eye_aspect_ratio
import numpy as np
import time
import cv2
import dlib
import fdetect
import csv
import datetime

print("--> Loading Face Predictor from ../dlibcascades/ ...")

try:
    detector = dlib.get_frontal_face_detector()
    # Using the specific path found in your code
    predictor_path = '../dlibcascades/shape_predictor_68_face_landmarks.dat'
    predictor = dlib.shape_predictor(predictor_path)
    print("--> Predictor loaded successfully.")

except RuntimeError:
    print("\n--------------------------------------------------")
    print("❌ CRITICAL ERROR: Predictor file not found!")
    print(f"Looked in: {predictor_path}")
    print("--------------------------------------------------")
    print("Please make sure the 'dlibcascades' folder exists")
    print("one level up, and contains the .dat file.")
    print("--------------------------------------------------\n")
    exit()

def face_pose(video_capture, facecascade):
    video = fdetect.video_read( config.FRAME_HEIGHT, config.FRAME_WIDTH )
    prev_time = 0
    new_time = 0

        # --- LOGGING SETUP ---
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    csv_filename = f"driver_log_{timestamp}.csv"
    file = open(csv_filename, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'EAR', 'State'])
    print(f"--> RECORDING DATA TO: {csv_filename}")
        # ---------------------
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # --- NEW CODE START ---
        if not ret: 
            break
        frame = cv2.resize(frame, None, fx=0.5, fy=0.5) 
        # --- NEW CODE END ---

        if ret:
            dets = detector(frame, 1)
            for k, d in enumerate(dets):
                # Get the landmarks/parts for the face in box d.
                shape = predictor(frame, d)
                # ... inside the loop ...
                shape = predictor(frame, d)

            # (The rest of your old code continues here: mid_x = ...)# --- CONVERT DLIB SHAPE TO NUMPY ---
                shape_np = np.zeros((68, 2), dtype="int")
                for i in range(0, 68):
                    shape_np[i] = (shape.part(i).x, shape.part(i).y)

                # --- DROWSINESS DETECTION ---
                # Extract coordinates (Left eye: 36-41, Right eye: 42-47)
                leftEye = shape_np[36:42]
                rightEye = shape_np[42:48]

                # Calculate EAR
                leftEAR = eye_aspect_ratio(leftEye)
                rightEAR = eye_aspect_ratio(rightEye)
                # ... inside the loop ...
                avgEAR = (leftEAR + rightEAR) / 2.0
                ear = (leftEAR + rightEAR) / 2.0
                now = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
                state = "DROWSY" if ear < config.EAR_THRESHOLD else "Active"
                writer.writerow([now, round(ear, 3), state])


                # --- ALARM SYSTEM START ---
                # Check if eye aspect ratio is below the blink threshold
                if avgEAR < config.EAR_THRESHOLD :
                # Draw a RED WARNING on the screen
                  cv2.putText(frame, "WAKE UP!", (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, config.COLOR_RED , 2)
                  print("!!! WAKE UP !!!")
                  # Play a Beep (Frequency 1000Hz, Duration 200ms)
                  print('\a')
                # --- ALARM SYSTEM END ---

                print(f"EAR: {avgEAR:.2f}")

                # Print to terminal to test
                print(f"EAR: {avgEAR:.2f}")

                # Draw on screen
                cv2.putText(frame, "EAR: {:.2f}".format(avgEAR), (200, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, config.COLOR_RED , 2)
                # -----------------------------
                mid_x = [(shape.part(1).x+shape.part(15).x)/2,
                         (shape.part(1).y+shape.part(15).y)/2]
                mid_y = [(shape.part(27).x+shape.part(66).x)/2,
                         (shape.part(27).y+shape.part(66).y)/2]
                nose = [shape.part(30).x, shape.part(30).y]
                final_x = 5*nose[0]-4*mid_x[0]
                final_y = 5*nose[1]-4*mid_y[1]
                print(f"Nose X: {nose[0]} | Gaze X: {int(final_x)}") # print nose,final_x  
                # Use config.COLOR_RED instead of (0, 0, 255)
                cv2.circle(frame, (int(final_x), int(final_y)), 2, config.COLOR_RED)
                cv2.circle(frame, (int(nose[0]), int(nose[1])), 2, config.COLOR_RED)

                # Use config.COLOR_BLUE instead of (255, 0, 0)
                cv2.line(frame, (int(nose[0]), int(nose[1])), (int(final_x), int(final_y)), config.COLOR_BLUE, 3)

                # --- FPS COUNTER ---
                new_time = time.time()
                fps = 1 / (new_time - prev_time)
                prev_time = new_time
                fps_text = "FPS: " + str(int(fps))
                cv2.putText(frame, fps_text, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, config.COLOR_GREEN , 2)
            # -------------------
            # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release video capture
    video.release()
    cv2.destroyAllWindows()

