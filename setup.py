from setuptools import setup, find_packages

setup(
    name="driver-drowsiness-ai",
    version="1.0.0",
    author="Aarav Mahara",
    description="A real-time AI system for driver drowsiness detection",
    packages=find_packages(),
    # --- ADD THIS LINE ---
    # List every single .py file you have (except setup.py)
    py_modules=[
        "ignite",
        "BCJA",
        "config",
        "head",
        "scenes",
        "drowsiness",
        "test",
        "utils",
        "getcascades",
        "gaze",
        "fdetect",
        "setup",
    ],
    # ---------------------
    install_requires=[
        "opencv-python",
        "dlib",
        "scipy",
        "imutils",
        "numpy",
        "pygame",
    ],
    entry_points={
        "console_scripts": [
            "drowsiness-detect=ignite:main",
        ],
    },
    python_requires=">=3.8",
)
