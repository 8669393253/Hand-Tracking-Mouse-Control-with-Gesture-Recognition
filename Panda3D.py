import cv2
import mediapipe as mp
import pyautogui
import time
import math

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Screen Resolution for mouse movement
screen_width, screen_height = pyautogui.size()

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Variables for gesture recognition
gesture_timeout = 0.5  # Time in seconds to debounce click detection
last_gesture_time = time.time()

# Function to calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Check if a finger is extended by comparing its landmark positions
def is_finger_extended(hand_landmarks, finger_tip, finger_mcp):
    return hand_landmarks.landmark[finger_tip].y < hand_landmarks.landmark[finger_mcp].y

# Function to check for pinch gesture (index and thumb close together for click)
def is_pinched(landmarks):
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    
    # Calculate distance between the thumb tip and index tip
    pinch_distance = distance(thumb_tip.x, thumb_tip.y, index_tip.x, index_tip.y)
    return pinch_distance < 0.05  # Threshold to detect pinch gesture

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame.")
        break
    
    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    
    # Convert the frame to RGB (MediaPipe uses RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame and get the hand landmarks
    result = hands.process(rgb_frame)
    
    # If hands are detected
    if result.multi_hand_landmarks:
        for landmarks in result.multi_hand_landmarks:
            # Get the position of the index finger tip (landmark 8) for cursor control
            index_finger_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_x = int(index_finger_tip.x * screen_width)
            index_y = int(index_finger_tip.y * screen_height)
            
            # Clamp the cursor position to the screen size
            index_x = max(0, min(screen_width - 1, index_x))
            index_y = max(0, min(screen_height - 1, index_y))
            
            # Move cursor with index finger
            pyautogui.moveTo(index_x, index_y)
            
            # Check for pinch gesture (index and thumb close together for click)
            if is_pinched(landmarks):
                if time.time() - last_gesture_time > gesture_timeout:  # Debounce click detection
                    pyautogui.click()  # Simulate a click
                    last_gesture_time = time.time()  # Update the last gesture time
                    print("Click detected!")

            # Draw hand landmarks on the frame (optional)
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Display the frame
    cv2.imshow("Hand Tracking", frame)
    
    # Exit loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()