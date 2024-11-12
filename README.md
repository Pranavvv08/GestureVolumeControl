# Hand Gesture Volume Control

This project is a computer vision application that controls the computer's volume using hand gestures, leveraging **OpenCV** and **MediaPipe** for real-time hand tracking and recognition. By adjusting the distance between specific hand landmarks, the program maps hand movement to volume changes on the computer.

## Features
- **Hand Tracking**: Uses MediaPipe to detect and track hand landmarks in real time.
- **Volume Control**: Calculates the distance between the index finger and thumb to set the system's audio volume.
- **Real-time Feedback**: Displays FPS, volume level, and hand landmarks on the video feed.

## Requirements
- **Python 3.x**
- **OpenCV** (`cv2`)
- **MediaPipe**
- **NumPy**
- **PyCaw** (Python Core Audio Windows library for volume control on Windows)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/hand-gesture-volume-control.git
   cd hand-gesture-volume-control
2. Install the required packages:
    ```bash
    pip install opencv-python mediapipe numpy comtypes pycaw

## Usage
1. Run the code with:
    ```bash
    python volumeControl.py
2. Adjust the volume by bringing your index finger and thumb closer or farther apart. The volume level will increase as the distance increases and decrease as the distance decreases.
## Controls
Press 'e' to exit the application.


## Code Overview

### `handTrackingModule.py`

This module contains the `HandDetector` class, which uses MediaPipe's hand-tracking solution to detect and track hand landmarks. The class provides methods to:

- Identify the position of hand landmarks in real time.
- Draw hand landmarks and connections on the image.

### `volumeControl.py`

This file integrates the hand-tracking data with PyCaw to control the system volume. It:

- Reads the position of the thumb and index finger.
- Calculates the distance between these landmarks.
- Maps the distance to a volume level using interpolation.

