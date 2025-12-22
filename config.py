# --- Camera Settings ---
CAMERA_INDEX = 0  # 0 for webcam, 1 for external
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# --- Drowsiness Thresholds ---
# EAR = Eye Aspect Ratio. Lower = Closed Eyes.
EAR_THRESHOLD = 0.25 
# Number of consecutive frames the eye must be closed to trigger alarm
CONSEC_FRAMES_THRESHOLD = 20 

# --- Colors (BGR Format) ---
COLOR_RED = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (255, 0, 0)
COLOR_YELLOW = (0, 255, 255)

# --- File Paths ---
SHAPE_PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
ALARM_SOUND_PATH = "alarm.wav"  # If you add sound later
