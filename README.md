# Hand Tracking Mouse Control with Gesture Recognition

This Python project uses **MediaPipe**, **OpenCV**, and **PyAutoGUI** to enable hand-tracking-based mouse control. The program tracks the position of the index finger and allows for simulating mouse clicks using a pinch gesture between the thumb and index finger. The movement of the index finger controls the cursor, and a pinch gesture triggers a click.

## Features

- **Mouse Control**: Move the mouse cursor based on the position of the index finger.
- **Click Simulation**: Use a pinch gesture (thumb and index finger close together) to simulate a mouse click.
- **Gesture Debouncing**: Prevents multiple clicks from being triggered in quick succession by implementing a time-based debounce mechanism.
- **Webcam Integration**: Uses your webcam for real-time hand tracking.

## Requirements

- Python 3.x
- `mediapipe` library
- `opencv-python` library
- `pyautogui` library

You can install the necessary libraries using `pip`:
pip install mediapipe opencv-python pyautogui

## Setup and Usage

### 1. **Clone the Repository or Download the Code**

You can clone the repository or download the Python script directly to your local machine.
git clone https://github.com/your-username/hand-tracking-mouse.git


### 2. **Run the Script**
Once you have the necessary dependencies installed, run the Python script from your terminal or command prompt:

python hand_tracking_mouse.py


This will open a webcam feed, track the position of your hand, and use your index finger to control the cursor.

### 3. **Gestures**

- **Move Cursor**: Move your index finger to control the mouse cursor position.
- **Click**: Pinch your index finger and thumb together to simulate a mouse click. The script has a debounce mechanism to ensure a single click is registered even if you pinch repeatedly.
  
### 4. **Exit the Program**

To stop the program, press the `q` key while the webcam feed window is active.

## Code Explanation

### 1. **Libraries**:

- **OpenCV**: Used to capture video from the webcam and to display frames with hand landmarks.
- **MediaPipe**: Provides hand tracking capabilities and allows us to access the positions of various hand landmarks.
- **PyAutoGUI**: Simulates mouse movements and clicks based on the hand gesture inputs.

### 2. **Core Functions**:

#### `distance(x1, y1, x2, y2)`
This function calculates the Euclidean distance between two points, used to check the distance between the thumb and index finger for the pinch gesture.

#### `is_finger_extended(hand_landmarks, finger_tip, finger_mcp)`
This function checks if a finger is extended based on the positions of its tip and metacarpal joint (MCP).

#### `is_pinched(landmarks)`
This function checks whether the thumb and index finger are close together (a pinch gesture). If the distance between the thumb tip and index tip is below a certain threshold, it considers the fingers as "pinched" and triggers a click.

### 3. **Hand Tracking and Mouse Control**:
- The script processes each webcam frame, detecting hand landmarks using MediaPipe.
- The position of the index finger's tip is mapped to the screen coordinates, controlling the mouse cursor.
- When a pinch gesture is detected, a click is simulated.

### 4. **Real-Time Webcam Processing**:
- The script captures frames from the webcam, processes them to detect hands, and uses the position of the index finger to control the mouse.
- It then checks if the pinch gesture is detected to simulate a mouse click.
- The frame is then displayed with landmarks drawn over it for visualization.

## Troubleshooting
- **Webcam Not Detected**: Ensure that your webcam is properly connected and recognized by your system.
- **Gestures Not Recognized Properly**: Ensure that your hand is in a clear, well-lit area, as hand tracking can be sensitive to lighting and hand positioning.
- **Clicking Delay**: The pinch gesture has a debounce time set to avoid multiple clicks. You can adjust the `gesture_timeout` variable to change the delay.

## Contributions
Feel free to fork the repository and contribute improvements or bug fixes. Suggestions for new features like adding more gestures or improving gesture detection are welcome.

## License
This project is open-source and available under the [MIT License](LICENSE).

**Author**: Tansen Siddharth Balpande 
**GitHub**: https://github.com/8669393253
