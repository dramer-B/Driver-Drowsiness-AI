import os
import cv2
import argparse
import logging
import BCJA  # Your main logic module


def setup_logging(verbose):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def get_args():
    parser = argparse.ArgumentParser(
        description="Driver Drowsiness Detection AI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-s",
        "--source",
        type=str,
        default="0",
        help="Path to video file OR camera index (e.g., '0' for webcam, 'test.mp4' for video)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable detailed debug logging"
    )
    return parser.parse_args()


# --- THIS IS THE NEW PART ---
def main():
    args = get_args()
    setup_logging(args.verbose)

    logging.info("--- STARTING ENGINE ---")

    source = args.source
    if source.isdigit():
        source = int(source)
        logging.info(f"Source detected as Webcam Index: {source}")
    else:
        logging.info(f"Source detected as Video File: {source}")

    os.environ["OPENCV_LOG_LEVEL"] = "OFF"

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        logging.critical(f"Could not open video source: {source}")
        return  # Changed from exit(1) to return so it handles cleanly

    logging.info("Video source loaded successfully. Launching AI...")

    try:
        BCJA.head_pose(cap)
    except KeyboardInterrupt:
        logging.warning("ENGINE STOPPED BY USER (Ctrl+C)")
    except Exception as e:
        logging.error(f"Unexpected Crash: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        logging.info("Resources released. Goodbye!")


if __name__ == "__main__":
    main()
