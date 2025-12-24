import os
import cv2
import argparse
import logging
import BCJA  # Your main logic module

# 1. Setup Professional Logging
def setup_logging(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

# 2. Define the "Control Panel" (Arguments)
def get_args():
    parser = argparse.ArgumentParser(
        description="Driver Drowsiness Detection AI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("-s", "--source", type=str, default="0",
                        help="Path to video file OR camera index (e.g., '0' for webcam, 'test.mp4' for video)")

    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable detailed debug logging")

    return parser.parse_args()

if __name__ == "__main__":
    # Parse arguments first
    args = get_args()
    setup_logging(args.verbose)

    logging.info("--- STARTING ENGINE ---")

    # 3. Handle Camera Source (Webcam vs File)
    source = args.source
    if source.isdigit():
        source = int(source)  # Convert "0" to 0 (integer) for webcam
        logging.info(f"Source detected as Webcam Index: {source}")
    else:
        logging.info(f"Source detected as Video File: {source}")

    # Set OpenCV log level to avoid spam
    os.environ["OPENCV_LOG_LEVEL"] = "OFF"

    # 4. Initialize Camera
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        logging.critical(f"Could not open video source: {source}")
        exit(1)

    logging.info("Video source loaded successfully. Launching AI...")

    # 5. Run the Main Loop
    try:
        # We pass the 'cap' object to your logic, just like before
        BCJA.head_pose(cap)

    except KeyboardInterrupt:
        logging.warning("ENGINE STOPPED BY USER (Ctrl+C)")
    except Exception as e:
        logging.error(f"Unexpected Crash: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        logging.info("Resources released. Goodbye!")
